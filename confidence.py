"""
confidence.py
Confidence scoring and evaluation layer for Module 5.
Assesses whether similarity-based predictions meet defined thresholds to ensure reliable responses.
"""

# Confidence score thresholds
HIGH_CONFIDENCE_THRESHOLD = 0.50
MEDIUM_CONFIDENCE_THRESHOLD = 0.25

# Named confidence levels
CONFIDENCE_HIGH = "high"
CONFIDENCE_MEDIUM = "medium"
CONFIDENCE_LOW = "low"


def evaluate_confidence(score: float, threshold: float = MEDIUM_CONFIDENCE_THRESHOLD) -> str:
    """
    Evaluates a similarity score and classifies it into high, medium, or low confidence.

    - score >= 0.50: High confidence
    - 0.25 <= score < 0.50 (or score >= threshold): Medium confidence
    - score < threshold: Low confidence
    """
    if score >= HIGH_CONFIDENCE_THRESHOLD:
        return CONFIDENCE_HIGH
    elif score >= threshold:
        return CONFIDENCE_MEDIUM
    else:
        return CONFIDENCE_LOW


def should_accept_prediction(score: float, threshold: float = MEDIUM_CONFIDENCE_THRESHOLD) -> bool:
    """
    Determines whether a similarity score is high enough to accept the predicted topic.
    Returns True if score meets or exceeds the threshold, False otherwise.
    """
    return score >= threshold
