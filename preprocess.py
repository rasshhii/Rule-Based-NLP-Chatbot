def normalize_text(text: str) -> str:
    """
    Normalizes the input text by:
    1. Converting all characters to lowercase.
    2. Removing leading and trailing whitespace.
    """
    if not isinstance(text, str):
        return ""
    return text.strip().lower()
