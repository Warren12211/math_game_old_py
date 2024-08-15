# math-game

# Imports custom modules named 'question_set_generator' and 'quiz_functions'.
# 'question_set_generator' generates list of random questions
# 'quiz_functions' is a couple of functions used in program
import question_set_generator as qsg
import quiz_functions as quiz

# Creates a list of addition questions by calling the 'question_set_generator' function.
# The arguments "add", 3, 3 set operation to addition, set 3 as the range, and set the number of questions.
add_questions = qsg.question_set_generator("add", 3, 3)

# Initializes a few variables:
# 'num_correct' to track the number of correct answers (starting at 0).
# 'incorrectly_answered' as an empty list to store questions that were answered incorrectly.
num_correct = 0
incorrectly_answered = []

# Makes a copy of the 'add_questions' list to 'current_question_set'.
# This is the set of questions that will be asked in the current session.
current_question_set = add_questions.copy()

# The main loop of the program, which continues until the user answers all questions correctly.
while num_correct != len(current_question_set):
    
    # If the user has answered at least one question correctly:
    if num_correct > 0:
        # Prompts the user to see if they want to practice the questions they got wrong.
        ask_practice = input("\nWould you like to practice the questions you got incorrect? [y/n]: ")
        
        # If the user inputs 'y', it will ask the incorrect questions again.
        if ask_practice == "y":
            quiz.AskQuestions(current_question_set, True)
    else:
        # If no questions were answered correctly or it's the first quiz:
        incorrectly_answered = []
        print("\n")
        
        # If all questions were answered incorrectky, informs user that they are restarting.
        if num_correct == 0:
            print("You answered all questions incorrectly. \nRestarting...")

        # Asks the set of questions and stores the results.
        quiz.AskQuestions(current_question_set)
        quiz.GiveResults(num_correct, incorrectly_answered)
