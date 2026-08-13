"""
main.py
Entry point for the Rule-Based NLP Chatbot (Module 1).
Manages the console interaction loop and connects normalization with rule processing.
"""

from preprocess import normalize_text
from rules import get_response, is_exit_command


def run_chatbot() -> None:
    """
    Main loop that continuously accepts user input and responds until an exit command is given.
    """
    print("=" * 50)
    print("Welcome to the Rule-Based Chatbot! (Module 1)")
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

        # Step 2: Determine and print response based on rules
        response = get_response(cleaned_input)
        print(f"Chatbot: {response}\n")

        # Step 3: Check if an exit command was triggered
        if is_exit_command(cleaned_input):
            break


if __name__ == "__main__":
    run_chatbot()
