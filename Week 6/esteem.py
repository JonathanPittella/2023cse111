"""
def get_user_response():
    while True:
        try:
            response_1 = int(input("I feel that I am a person of worth, at least on an equal plane with others. (0-3) -> "))
            if 0 <= response_1 <= 3:
                return response_1
            else:
                print("Invalid response. Please enter a number between 0 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        
            response_2 = int(input("I feel that I have a number of good qualities. (0-3) -> "))
            if 0 <= response_2 <= 3:
                return response_2
            else:
                print("Invalid response. Please enter a number between 0 and 3.")
            except ValueError:
                print("Invalid input. Please enter a number.")

def calculate_self_esteem_grade(response_1, response_2):
    if response_1 == 3:
        return "Strongly Agree"
    elif response_1 == 2:
        return "Agree"
    elif response_1 == 1:
        return "Disagree"
    else:
        return "Strongly Disagree"
    
    if response_2 == 3:
        return "Strongly Agree"
    elif response_2 == 2:
        return "Agree"
    elif response_2 == 1:
        return "Disagree"
    else:
        "Strongly Disagree"

def main():
    print("Welcome to the Self-Esteem Grader!")
    print("Please respond to the following statement:")
    
    user_response = get_user_response()
    self_esteem_grade = calculate_self_esteem_grade(user_response)
    
    print(f"Your self-esteem grade: {self_esteem_grade}")

if __name__ == "__main__":
    main()
"""
"""
def get_user_response(statement):
    while True:
        try:
            response = int(input(f"{statement} (0-3) -> "))
            if 0 <= response <= 3:
                return response
            else:
                print("Invalid response. Please enter a number between 0 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_self_esteem_grade(response):
    if response == 3:
        return "Strongly Agree"
    elif response == 2:
        return "Agree"
    elif response == 1:
        return "Disagree"
    else:
        return "Strongly Disagree"

def main():
    print("Welcome to the Self-Esteem Grader!")
    
    statement_1 = "I feel that I am a person of worth, at least on an equal plane with others."
    response_1 = get_user_response(statement_1)
    grade_1 = calculate_self_esteem_grade(response_1)
    
    statement_2 = "I feel that I have a number of good qualities."
    response_2 = get_user_response(statement_2)
    grade_2 = calculate_self_esteem_grade(response_2)

    statement_3 = "All in all, I am inclined to feel that I am a failure."
    response_3 = get_user_response(statement_3)
    grade_3 = calculate_self_esteem_grade(response_3)

    statement_4 = "I am able to do things as well as most other people."
    response_4 = get_user_response(statement_4)
    grade_4 = calculate_self_esteem_grade(response_4)

    statement_5 = "I feel I do not have much to be proud of."
    response_5 = get_user_response(statement_5)
    grade_5 = calculate_self_esteem_grade(response_5)

    statement_6 = "I take a positive attitude toward myself."
    response_6 = get_user_response(statement_6)
    grade_6 = calculate_self_esteem_grade(response_6)

    statement_7 = "On the whole, I am satisfied with myself."
    response_7 = get_user_response(statement_7)
    grade_7 = calculate_self_esteem_grade(response_7)

    statement_8 = "I wish I could have more respect for myself."
    response_8 = get_user_response(statement_8)
    grade_8 = calculate_self_esteem_grade(response_8)

    statement_9 = "I certainly feel useless at times."
    response_9 = get_user_response(statement_9)
    grade_9 = calculate_self_esteem_grade(response_9)

    statement_10 = "At times I think I am no good at all."
    response_10 = get_user_response(statement_10)
    grade_10 = calculate_self_esteem_grade(response_10)

    print(f"Your self-esteem grade for statement 1: {grade_1}")
    print(f"Your self-esteem grade for statement 2: {grade_2}")
    print(f"Your self-esteem grade for statement 2: {grade_3}")
    print(f"Your self-esteem grade for statement 2: {grade_4}")
    print(f"Your self-esteem grade for statement 2: {grade_5}")
    print(f"Your self-esteem grade for statement 2: {grade_6}")
    print(f"Your self-esteem grade for statement 2: {grade_7}")
    print(f"Your self-esteem grade for statement 2: {grade_8}")
    print(f"Your self-esteem grade for statement 2: {grade_9}")
    print(f"Your self-esteem grade for statement 2: {grade_10}")

if __name__ == "__main__":
    main()
"""
"""
def calculate_self_esteem_score(responses):
    positive_statements = [0, 1, 3, 5, 6]
    negative_statements = [2, 4, 7, 8, 9]
    
    total_score = 0
    
    for i in range(len(responses)):
        if i in positive_statements:
            total_score += responses[i]
        elif i in negative_statements:
            total_score += (3 - responses[i])
    
    return total_score

def get_user_responses():
    responses = []
    for i in range(1, 11):
        while True:
            try:
                response = int(input(f"Statement {i}: Enter your response (0-3) -> "))
                if 0 <= response <= 3:
                    responses.append(response)
                    break
                else:
                    print("Invalid response. Please enter a number between 0 and 3.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    return responses

def main():
    print("Welcome to the Rosenberg Self-Esteem Scale Calculator!")
    print("Please respond to the following statements from 0 to 3 (0=Strongly Disagree, 1=Disagree, 2=Agree, 3=Strongly Agree):")
    
    user_responses = get_user_responses()
    self_esteem_score = calculate_self_esteem_score(user_responses)
    
    print(f"Your self-esteem score is: {self_esteem_score}")
    
    if self_esteem_score < 15:
        print("You may have a problematic low self-esteem. Please consider talking to a mental health professional.")
    else:
        print("Your self-esteem is relatively healthy!")

if __name__ == "__main__":
    main()
"""
# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

def main():
    print("This program is an implementation of the Rosenberg")
    print("Self-Esteem Scale. This program will show you ten")
    print("statements that you could possibly apply to yourself.")
    print("Please rate how much you agree with each of the")
    print("statements by responding with one of these four letters:")
    print()
    print("D means you strongly disagree with the statement.")
    print("d means you disagree with the statement.")
    print("a means you agree with the statement.")
    print("A means you strongly agree with the statement.")
    print()

    score = 0
    score += ask_positive_question(
        "1. I feel that I am a person of worth, at least on an"
        " equal plane with others.")
    score += ask_positive_question(
        "2. I feel that I have a number of good qualities.")
    score += ask_negative_question(
        "3. All in all, I am inclined to feel that I am a failure.")
    score += ask_positive_question(
        "4. I am able to do things as well as most other people.")
    score += ask_negative_question(
        "5. I feel I do not have much to be proud of.")
    score += ask_positive_question(
        "6. I take a positive attitude toward myself.")
    score += ask_positive_question(
        "7. On the whole, I am satisfied with myself.")
    score += ask_negative_question(
        "8. I wish I could have more respect for myself.")
    score += ask_negative_question(
        "9. I certainly feel useless at times.")
    score += ask_negative_question(
        "10. At times I think I am no good at all.")

    print()
    print(f"Your score is {score}.")
    print("A score below 15 may indicate problematic low self-esteem.")


def ask_positive_question(statement):
    """Display one statement to the user and get the user's response.
    Then determine the score for the response and return the score.

    Parameters
        statement: The statement to show the user.
        pos_or_neg: Either the constant POSITIVE or NEGATIVE.
    Return: the score from the user's response to the statement.
    """
    print(statement)
    answer = input("   Enter D, d, a, or A: ")
    score = 0
    if answer == 'D':
        score = 0
    elif answer == 'd':
        score = 1
    elif answer == 'a':
        score = 2
    elif answer == 'A':
        score = 3
    return score

def ask_negative_question(statement):
    """Display one statement to the user and get the user's response.
    Then determine the score for the response and return the score.

    Parameters
        statement: The statement to show the user.
        pos_or_neg: Either the constant POSITIVE or NEGATIVE.
    Return: the score from the user's response to the statement.
    """
    print(statement)
    answer = input("   Enter D, d, a, or A: ")
    score = 0
    if answer == 'D':
        score = 3
    elif answer == 'd':
        score = 2
    elif answer == 'a':
        score = 1
    elif answer == 'A':
        score = 0
    return score


# If this file was executed like this:
# > python esteem.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()