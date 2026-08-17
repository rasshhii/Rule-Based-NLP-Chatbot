"""
main.py
Entry point for the Rule-Based NLP Chatbot (Module 3).
Coordinates user input, preprocessing, intent detection, topic detection, and response generation.
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
from knowledge_base import get_knowledge

# Unsupported knowledge topic guidance response
UNSUPPORTED_TOPIC_RESPONSE = (
    "I can currently answer questions about AI, Machine Learning, NLP, Python, and AI Engineering. "
    "Please ask about one of these topics."
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
    For knowledge questions, dynamically resolves the topic and retrieves the answer.
    """
    # Dynamic response generation for knowledge-base questions
    if intent == INTENT_KNOWLEDGE_QUESTION:
        topic = detect_topic(cleaned_input)
        if topic:
            answer = get_knowledge(topic)
            if answer:
                return answer
        return UNSUPPORTED_TOPIC_RESPONSE

    # Static response lookup for standard conversational intents
    return RESPONSES.get(intent, RESPONSES[INTENT_UNKNOWN])


def run_chatbot() -> None:
    """
    Main loop that continuously accepts user input, processes intent and topic,
    and responds until an exit/goodbye intent is triggered.
    """
    print("=" * 50)
    print("Welcome to the Rule-Based Chatbot! (Module 3)")
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
