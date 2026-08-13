"""
rules.py
Contains predefined rule keywords and matching functions for Module 1.
"""

# Predefined keywords for basic rule matching
GREETING_KEYWORDS = ["hello", "hi", "hey", "greetings", "good morning", "good evening", "good afternoon"]
GOODBYE_KEYWORDS = ["bye", "goodbye", "exit", "quit", "see you"]
HELP_KEYWORDS = ["help", "what can you do", "commands", "options"]


def is_exit_command(cleaned_input: str) -> bool:
    """
    Checks if the normalized user input matches any exit/goodbye keywords.
    """
    return cleaned_input in GOODBYE_KEYWORDS


def get_response(cleaned_input: str) -> str:
    """
    Evaluates the normalized user input against simple rules and returns an appropriate response.
    """
    # 1. Empty input rule
    if not cleaned_input:
        return "Please say something! Type 'help' if you're not sure what to ask."

    # 2. Goodbye / Exit rule
    if is_exit_command(cleaned_input):
        return "Goodbye! Have a great day!"

    # 3. Greeting rule (exact match or starts with common greeting)
    if cleaned_input in GREETING_KEYWORDS or any(cleaned_input.startswith(f"{word} ") for word in ["hello", "hi", "hey"]):
        return "Hello! How can I assist you today?"

    # 4. Help rule
    if cleaned_input in HELP_KEYWORDS or "help" in cleaned_input:
        return (
            "Here is what I can do:\n"
            "  - Greet you (e.g., 'hello', 'hi', 'hey')\n"
            "  - Provide assistance (e.g., 'help')\n"
            "  - End the conversation (e.g., 'bye', 'goodbye', 'exit', 'quit')"
        )

    # 5. Default fallback rule
    return "I'm sorry, I don't understand that yet. Type 'help' to see what I can do."
