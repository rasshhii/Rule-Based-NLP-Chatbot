"""
topic_detector.py
Topic detection layer for Module 3.
Matches normalized user input to domain topics defined in knowledge_base.py.
"""

import re
from knowledge_base import KNOWLEDGE_BASE


def detect_topic(cleaned_input: str) -> str | None:
    """
    Scans the normalized user input for keywords associated with knowledge base topics.
    Returns the exact topic name from KNOWLEDGE_BASE if matched, or None if no topic is found.
    """
    if not cleaned_input:
        return None

    # Collect all (keyword, topic) pairs from KNOWLEDGE_BASE
    keyword_topic_pairs = []
    for topic, data in KNOWLEDGE_BASE.items():
        for keyword in data.get("keywords", []):
            keyword_topic_pairs.append((keyword.lower(), topic))

    # Sort keywords by length in descending order so longer phrases match before shorter ones
    # Example: "ai engineer" is checked before "ai"
    keyword_topic_pairs.sort(key=lambda item: len(item[0]), reverse=True)

    # Check each keyword against user input using word boundaries
    for keyword, topic in keyword_topic_pairs:
        # \b ensures whole-word/phrase matching (prevents 'ai' matching inside 'explain')
        pattern = rf"\b{re.escape(keyword)}\b"
        if re.search(pattern, cleaned_input):
            return topic

    return None
