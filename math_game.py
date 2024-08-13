# math-game

# Imports needed libraries
from random import choice

# My custom module
import question_set_generator as qsg

# Creates a list of question, addition and top_num is 10
add_questions = qsg.question_set_generator("add", 10)

# Defining couple of lists
# List of questions that were answered correctly, and incorrectly,
# And list that's used to store which questions the user needs to learn
correctly_answered = []
incorrectly_answered = []
learn_list = []

# The current set of question being used
current_question_set = add_questions.copy()

for x in range(11):

    # Selects a random question out of the set
    current_question = choice(current_question_set)

    # Asks user answer to question
    user_answer = input(f"What is {current_question.string}?: ")

    # If user_answer = answer, changes status of question to answered correctly
    # Removes it from question set so it isn't asked again
    if user_answer == str(current_question.answer):

        # Sets status
        current_question.status = "answered_correctly"

        # Adds to correctly answered list
        correctly_answered.append(current_question)
        
        # Removes from question set
        current_question_set.remove(current_question)

    # Otherwise
    else:
        # Sets status
        current_question.status = "incorrect"

        # Adds to incorrectly answered list
        incorrectly_answered.append(current_question)

        # Removes from question set
        current_question_set.remove(current_question)


print(len(correctly_answered))
print(type(len(correctly_answered)))

if len(correctly_answered) == 1 or len(incorrectly_answered) == 1:
    question_string = "question"
else:
    question_string = "questions"

print(f"\nYou got {len(correctly_answered)} {question_string} right!")
print(f"You got {len(incorrectly_answered)} {question_string} questions wrong.")

practice_list = incorrectly_answered.copy()

practice_incorrect_questions = input("\nWould you like to practice the questions you got incorrect? [y/n]: ")

if practice_incorrect_questions == "y":

    for item in incorrectly_answered:
        item.status = "incorrect_0"

    while len(incorrectly_answered) != 0:

        # Gets a random question
        current_question = choice(incorrectly_answered)

        # Gets user input
        user_answer = input(f"What is {current_question.string}?: ")

        # If the user's answer equals the correct answer
        if user_answer == current_question.answer:

            # Remove from incorrectly answered list
            print(f"Correct! The answer is {user_answer}!")
            incorrectly_answered.remove(current_question)

        # If the user's answer does not equal the correct answer
        else:

            # Gets status on how many times question answered incorrectly
            incorrect_number = current_question.status.replace("incorrect_", "")

            # If answered incorrectly 3 times
            if incorrect_number == "3":

                # Tell user answer
                print(f"You got this wrong too many times. The correct answer is {current_question.answer}.")

                # Add to need to learn list
                learn_list.append(current_question)

                # Remove from incorrectly answered list
                incorrectly_answered.remove(current_question)

            # If not answered incorrectky 3 times 
            else:

                # Tell user answer
                print(f"Incorrect. The correct answer is {current_question.answer}")

                # Adds one to incorrectly answered status
                incorrect_number = int(incorrect_number)
                incorrect_number += 1

                # Sets status
                current_question.status = f"incorrect_{str(incorrect_number)}"

print(f"You need to learn: ")
for item in learn_list:
    print(str(item))

print(f"You need to practice: ")
for item in practice_list:
    print(str(item))

