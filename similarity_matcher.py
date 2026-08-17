"""
similarity_matcher.py
Similarity-based topic matching layer for Module 4.
Uses TF-IDF vectorization and cosine similarity to find the most relevant
knowledge-base topic when exact keyword/topic matching does not match.
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Reference/example phrases for each existing knowledge base topic
TOPIC_REFERENCE_PHRASES = {
    "AI": [
        "what is artificial intelligence",
        "explain artificial intelligence",
        "intelligent machines and systems",
        "computers simulating human intelligence",
        "systems mimicking human intelligence and cognition",
    ],
    "Machine Learning": [
        "what is machine learning",
        "explain machine learning",
        "algorithms learn patterns from data",
        "learning from data and examples",
        "how machines learn from experience",
    ],
    "NLP": [
        "what is natural language processing",
        "explain NLP",
        "explain natural language processing",
        "computers understanding human language",
        "processing human language and speech",
        "text and language understanding",
    ],
    "Python": [
        "what is Python",
        "explain Python programming",
        "Python programming language",
        "programming with Python",
        "popular programming language for AI and data science",
    ],
    "AI Engineer": [
        "what is an AI engineer",
        "explain AI engineering",
        "what does an AI engineer do",
        "building AI applications and systems",
        "someone who builds artificial intelligence systems",
    ],
}

# Flatten reference phrases and map each phrase index to its topic name
_CORPUS = []
_PHRASE_TOPICS = []
for topic, phrases in TOPIC_REFERENCE_PHRASES.items():
    for phrase in phrases:
        _CORPUS.append(phrase)
        _PHRASE_TOPICS.append(topic)

# Initialize and fit TF-IDF vectorizer using standard English stop-words
_VECTORIZER = TfidfVectorizer(stop_words="english").fit(_CORPUS)
_CORPUS_VECTORS = _VECTORIZER.transform(_CORPUS)


def find_similar_topic(cleaned_input: str, threshold: float = 0.25) -> tuple[str | None, float]:
    """
    Computes TF-IDF cosine similarity between the user input and reference phrases.
    Returns (topic_name, similarity_score) if the highest score >= threshold,
    otherwise returns (None, highest_similarity_score).
    """
    # 1. Return (None, 0.0) for empty or whitespace-only input
    if not cleaned_input or not cleaned_input.strip():
        return None, 0.0

    # 2. Convert user input into TF-IDF vector
    user_vector = _VECTORIZER.transform([cleaned_input])

    # 3. Calculate cosine similarity against all reference phrase vectors
    similarity_scores = cosine_similarity(user_vector, _CORPUS_VECTORS)[0]

    # 4. Find the highest similarity score and its index
    max_index = similarity_scores.argmax()
    max_score = float(similarity_scores[max_index])

    # 5. Return matched topic if score meets or exceeds threshold
    if max_score >= threshold:
        matched_topic = _PHRASE_TOPICS[max_index]
        return matched_topic, max_score

    # 6. Otherwise return None with the highest similarity score
    return None, max_score
