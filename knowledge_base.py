"""
knowledge_base.py
Knowledge base layer for Module 3.
Stores structured domain knowledge and keyword metadata for predefined topics.
"""

# Dictionary storing knowledge topics, associated keywords, and beginner-friendly answers.
KNOWLEDGE_BASE = {
    "AI": {
        "keywords": ["ai", "artificial intelligence", "intelligent machines"],
        "answer": (
            "Artificial Intelligence (AI) is a branch of computer science that enables "
            "machines to simulate human intelligence, including learning, reasoning, and problem-solving."
        ),
    },
    "Machine Learning": {
        "keywords": ["machine learning", "ml", "supervised learning", "unsupervised learning"],
        "answer": (
            "Machine Learning (ML) is a subset of AI where algorithms learn patterns from data "
            "and improve their performance over time without being explicitly hardcoded."
        ),
    },
    "NLP": {
        "keywords": ["nlp", "natural language processing", "text processing", "language understanding"],
        "answer": (
            "Natural Language Processing (NLP) is a branch of AI focused on helping computers "
            "understand, interpret, and generate human languages."
        ),
    },
    "Python": {
        "keywords": ["python", "python programming", "python language"],
        "answer": (
            "Python is a versatile, high-level programming language known for its simple syntax "
            "and wide adoption in AI, data science, and web development."
        ),
    },
    "AI Engineer": {
        "keywords": [
            "ai engineer", "artificial intelligence engineer", "ai developer",
            "building ai applications", "builds ai applications"
        ],
        "answer": (
            "An AI Engineer is a software specialist who designs, builds, and deploys "
            "AI models and applications to solve complex practical problems."
        ),
    },
}


def get_knowledge(topic: str) -> str | None:
    """
    Retrieves the answer for a given topic from the knowledge base.
    Returns the answer string if the topic exists, or None if it does not.
    """
    if not isinstance(topic, str):
        return None

    # Check for direct key match
    if topic in KNOWLEDGE_BASE:
        return KNOWLEDGE_BASE[topic]["answer"]

    # Case-insensitive / normalized lookup fallback
    topic_normalized = topic.strip().lower()
    for key, data in KNOWLEDGE_BASE.items():
        if key.lower() == topic_normalized:
            return data["answer"]

    return None
