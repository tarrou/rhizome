from typing import List

def get_input_choices(question: str, choices: List[str], case_sensitive: bool = False, invalid_msg: str = "") -> str:
    """
    A helper function to present choices and not stop asking until 
    a valid answer is given.

    question: a string asking the question and defining available choices
    choices: a list of valid answers to the question
    case_sensitive: True is answers are case_sensitive
    invalid_msg: a string displayed when invalid answer chosen
    """

    if not case_sensitive:
        choices = [choice.lower() for choice in choices]

    while True:
        user_choice = input(question)
        for choice in choices:
            if user_choice == choice:
                return user_choice
        print(invalid_msg)

