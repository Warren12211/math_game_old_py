# math-game

# Imports needed libraries
from random import choice

# My custom module
import question_set_generator as qsg

# Creates a list of questions for addition with 3 questions and top_num as 3
add_questions = qsg.question_set_generator("add", 3, 3)

# Defining several lists and variables
# List of questions that were answered correctly and incorrectly,
# And a list used to store which questions the user needs to learn
num_correct = 0
incorrectly_answered = []
last_answer = None


def GiveResults(num_correct, incorrectly_answered):
    # Print the results of the quiz, showing the number of correct and incorrect answers.
    # Determine the correct word for singular or plural
    if num_correct == 1:
        question_string = "question"
    else:
        question_string = "questions"

    # Print number of correct answers
    print(f"\nYou got {num_correct} {question_string} right!")
    
    # Print number of incorrect answers
    if num_correct == 1:
        question_string = "question"
    else:
        question_string = "questions"

    print(f"You got {len(incorrectly_answered)} {question_string} wrong.")


def AskQuestions(questions, practice=False):
    # Ask the questions to the user and check their answers.
    # Optionally, provide practice on incorrectly answered questions.
    for i in range(len(questions)):
        if not questions[i].correct:
            # Asks user the answer to the question
            user_answer = input(f"What is {questions[i].string}?: ")

            # If user_answer is correct, change the status of the question to answered correctly
            # Remove it from the question set so it isn't asked again
            if user_answer == str(questions[i].answer):
                # Correct answer
                questions[i].correct = True
                global num_correct
                num_correct += 1
            else:
                # Incorrect answer
                incorrectly_answered.append(questions[i])
                questions[i].attempts += 1

            if practice:
                if questions[i].correct:
                    print("Correct!")
                else:
                    if questions[i].attempts == 3:
                        print(f"You got this wrong too many times. The correct answer is {questions[i].answer}.")
                    else:
                        print(f"Incorrect. The correct answer is {questions[i].answer}.")
                    questions[i].attempts += 1
                    questions[i].correct = False

    return questions


# The current set of questions being used
current_question_set = add_questions.copy()

while num_correct != len(current_question_set):
    if num_correct > 0:
        ask_practice = input("\nWould you like to practice the questions you got incorrect? [y/n]: ")
        if ask_practice == "y":
            AskQuestions(current_question_set, True)
    else:
        # First quiz or all answers were incorrect
        incorrectly_answered = []
        print("\n")
        AskQuestions(current_question_set)
        GiveResults(num_correct, incorrectly_answered)
