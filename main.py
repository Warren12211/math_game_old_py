# ---------- Imports needed modules ----------

import random
import question_set_generator as qsg

# ---------- Initialize Functions ----------

# This function asks the list of questions passed to it
# It has different ways, based on whether or not the user is in practice mode
def AskQuestions(list, practice=False):

    # correct keeps track of number of questions answered correctly
    # incorrect is a list that contains the questions answered incorrectly
    correct = 0
    incorrect = []

    # If the user doesn't want to practice
    if practice == False:
        # It asks every question in the list
        for i in range(len(list)):
            
            # Equals current question in the list
            current_question = list[i]

            # Get user input
            user_answer = input(f"What is {current_question.string}?: ")

            # if user_answer = current_question
            if user_answer == current_question.answer:
                # Add one to correct
                correct += 1
            else:
                # add to incorrect list
                incorrect.append(list[i])
    # If practice is True
    else:
        # While there are still questions in the list
        while len(list) != 0:

            # Select random question from the list
            current_question = random.choice(list)
            
            # Get user input
            user_answer = input(f"What is {current_question.string}?: ")

            # If user answer equals correct answer
            if user_answer == current_question.answer:
                print("Correct!\n")

                # Remove from list, so it's not asked again
                list.remove(current_question)
            else:
                print(f"Incorrect. The correct answer is {current_question.answer}.\n")

                # Adds one to the attempt count
                current_question.attempts += 1

                # If attempt count equals 3
                if current_question.attempts == 3:
                    print("You got this wrong too many times.\n")

                    # Remove from list so not asked again
                    list.remove(current_question)

    # Returns incorrect, and correct, so they can be used by the GiveResults() function
    return incorrect, correct

# Takes two args, an int, and a list
# It gives the results on the number of questions answered, based on the
# vars from the AskQuestions() function
def GiveResults(correct, incorrect):

    # If correct equals 1
    if correct == 1:
        # Set question_string to singular, "question"
        question_string = "question"
    else:
        # Set question_string to plural, "questions"
        question_string = "questions"

    # Gives user results
    print(f"\nYou got {correct} {str(question_string)} right!")

    # Same as above, but for the length of incorrectly answered questions
    if (len(incorrect)) == 1:
        question_string = "question"
    else:
        question_string = "questions"

    print(f"You got {len(incorrect)} {str(question_string)} wrong.\n")

# Creates a list of random questions
add_questions = qsg.QuestionSetGenerator("add", 5, 10)
question_list = add_questions.copy()

# Asks questions, and returns the number of questions answered correctly, and the list of incorrectly answered questions
incorrectly_answered, num_correct = AskQuestions(question_list)

# Gives quiz results based on variables returned by AskQuestions()
GiveResults(num_correct, incorrectly_answered)

# If questions were answered incorrectly
if len(incorrectly_answered) != 0:

    # Ask user if they would like to practice incorrect questions
    ask_practice = input("Would you like to practice the questions you got incorrect?: ").strip().lower()

    # If yes, ask incorrect questions
    if ask_practice == 'y':
        AskQuestions(incorrectly_answered, practice=True)