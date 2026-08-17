"""
intent_detector.py
Dedicated intent detection layer for Module 2.
Maps normalized user inputs to predefined intent categories using rule-based pattern matching.
"""

# Intent category constants
INTENT_GREETING = "greeting"
INTENT_HELP = "help"
INTENT_GOODBYE = "goodbye"
INTENT_ABOUT_BOT = "about_bot"
INTENT_KNOWLEDGE_QUESTION = "knowledge_question"
INTENT_UNKNOWN = "unknown"

from topic_detector import detect_topic
from similarity_matcher import find_similar_topic

# Rule-based patterns and keywords for each intent
GREETING_KEYWORDS = [
    "hello", "hi", "hey", "greetings",
    "good morning", "good evening", "good afternoon"
]

GOODBYE_KEYWORDS = [
    "bye", "goodbye", "see you", "exit",
    "quit", "cya", "farewell"
]

HELP_KEYWORDS = [
    "help", "can you help me", "what can you do",
    "commands", "options", "how do you work"
]

ABOUT_BOT_KEYWORDS = [
    "who are you", "what are you", "tell me about yourself",
    "about yourself", "what is your name", "who made you"
]

QUESTION_PATTERNS = [
    "what is", "what are", "what does", "tell me about",
    "explain", "describe", "define", "meaning of"
]


def detect_intent(cleaned_input: str) -> str:
    """
    Analyzes the normalized (lowercase, stripped) user input and returns the detected intent name.
    """
    # 1. Handle empty input
    if not cleaned_input:
        return INTENT_UNKNOWN

    # 2. Check for Goodbye / Exit intent
    if cleaned_input in GOODBYE_KEYWORDS:
        return INTENT_GOODBYE

    # 3. Check for About Bot intent (exact phrase match or substring match)
    for pattern in ABOUT_BOT_KEYWORDS:
        if pattern in cleaned_input:
            return INTENT_ABOUT_BOT

    # 4. Check for Help intent
    for pattern in HELP_KEYWORDS:
        if pattern in cleaned_input:
            return INTENT_HELP

    # 5. Check for Greeting intent
    if cleaned_input in GREETING_KEYWORDS or any(
        cleaned_input.startswith(f"{word} ") for word in ["hello", "hi", "hey"]
    ):
        return INTENT_GREETING

    # 6. Check for Knowledge Question intent (exact topic match, similarity match, or question phrasing)
    if (
        detect_topic(cleaned_input) is not None
        or find_similar_topic(cleaned_input)[0] is not None
        or any(pattern in cleaned_input for pattern in QUESTION_PATTERNS)
    ):
        return INTENT_KNOWLEDGE_QUESTION

    # 7. Fallback if no rules matched
    return INTENT_UNKNOWN
