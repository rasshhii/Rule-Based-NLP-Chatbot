"""
main.py
Entry point for the Rule-Based NLP Chatbot (Module 5).
Coordinates user input, preprocessing, intent detection, exact topic detection,
similarity-based fallback matching, confidence scoring, and smart fallback responses.
"""

from preprocess import normalize_text
from intent_detector import (
    detect_intent,
    INTENT_GREETING,
    INTENT_HELP,
    INTENT_GOODBYE,
    INTENT_ABOUT_BOT,
    INTENT_KNOWLEDGE_QUESTION,
    INTENT_UNKNOWN,
)
from topic_detector import detect_topic
from similarity_matcher import find_similar_topic
from confidence import should_accept_prediction
from knowledge_base import get_knowledge

# Smart fallback response for low-confidence or unsupported knowledge topics
SMART_FALLBACK_RESPONSE = (
    "I'm not confident I understood the topic. I can currently help with AI, "
    "Machine Learning, NLP, Python, and AI Engineering. Could you rephrase your "
    "question or mention one of these topics?"
)

# Intent to static response mapping (for conversational intents)
RESPONSES = {
    INTENT_GREETING: "Hello! How can I assist you today?",
    INTENT_HELP: (
        "Here is what I can do:\n"
        "  - Greet you (e.g., 'hello', 'hi', 'hey')\n"
        "  - Provide assistance (e.g., 'help')\n"
        "  - Tell you about myself (e.g., 'who are you')\n"
        "  - Answer questions about AI, Machine Learning, NLP, Python, and AI Engineering\n"
        "  - End the conversation (e.g., 'bye', 'goodbye', 'exit', 'quit')"
    ),
    INTENT_GOODBYE: "Goodbye! Have a great day!",
    INTENT_ABOUT_BOT: "I am a rule-based NLP chatbot designed to understand basic user intents.",
    INTENT_UNKNOWN: "I'm sorry, I don't understand that yet. Type 'help' to see what I can do.",
}


def get_response(intent: str, cleaned_input: str = "") -> str:
    """
    Selects and returns an appropriate response based on the detected intent.

    For knowledge questions:
    1. First attempts exact topic matching via detect_topic().
    2. If exact matching fails, falls back to TF-IDF similarity via find_similar_topic().
    3. Evaluates prediction confidence using should_accept_prediction().
    4. If confidence is sufficient, returns the knowledge answer; otherwise returns smart fallback.
    """
    # Dynamic response generation for knowledge-base questions
    if intent == INTENT_KNOWLEDGE_QUESTION:
        # Step 1: Exact keyword/topic matching takes first priority
        topic = detect_topic(cleaned_input)
        if topic:
            answer = get_knowledge(topic)
            if answer:
                return answer

        # Step 2: Fall back to TF-IDF cosine similarity matching
        similar_topic, score = find_similar_topic(cleaned_input)

        # Step 3: Confidence evaluation layer decides whether to accept prediction
        if should_accept_prediction(score) and similar_topic:
            answer = get_knowledge(similar_topic)
            if answer:
                return answer

        # Step 4: Low confidence / unsupported topic smart fallback
        return SMART_FALLBACK_RESPONSE

    # Static response lookup for standard conversational intents
    return RESPONSES.get(intent, RESPONSES[INTENT_UNKNOWN])


def run_chatbot() -> None:
    """
    Main loop that continuously accepts user input, processes intent, topic,
    similarity matching, and confidence evaluation, and responds until exit.
    """
    print("=" * 50)
    print("Welcome to the Rule-Based Chatbot! (Module 5)")
    print("Type 'help' for available commands or 'exit' to quit.")
    print("=" * 50)
    print()

    while True:
        try:
            # Continuously accept user input from the console
            user_input = input("You: ")
        except (KeyboardInterrupt, EOFError):
            print("\n\nChatbot: Goodbye! (Session closed)")
            break

        # Step 1: Normalize user input (lowercase & whitespace cleanup)
        cleaned_input = normalize_text(user_input)

        # Step 2: Detect intent (Intent Detection Layer)
        intent = detect_intent(cleaned_input)

        # Step 3: Select response (Response Generation Layer)
        response = get_response(intent, cleaned_input)
        print(f"Chatbot: {response}\n")

        # Step 4: Check if conversation should end
        if intent == INTENT_GOODBYE:
            break


if __name__ == "__main__":
    run_chatbot()
