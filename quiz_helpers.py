# quiz_helpers.py

def GiveResults(num_correct, incorrectly_answered):
    """
    Print the results of the quiz, showing the number of correct and incorrect answers.
    """
    # Determine whether to use "question" or "questions" based on the count
    if num_correct == 1:
        question_string = "question"
    else:
        question_string = "questions"

    # Print the number of questions answered correctly
    print(f"\nYou got {num_correct} {question_string} right!")

    # Determine whether to use "question" or "questions" for incorrect answers
    if len(incorrectly_answered) == 1:
        question_string = "question"
    else:
        question_string = "questions"

    # Print the number of questions answered incorrectly
    print(f"You got {len(incorrectly_answered)} {question_string} wrong.")

def AskQuestions(questions, practice=False):
    """
    Ask each question in the list to the user, check their answers, and provide feedback.
    Optionally provide practice on incorrectly answered questions.
    
    Parameters:
    questions (list): List of Question objects to ask.
    practice (bool): If True, provide feedback on incorrect answers and allow practice.
    
    Returns:
    num_correct (int): Number of questions answered correctly.
    incorrectly_answered (list): List of Question objects that were answered incorrectly.
    """
    num_correct = 0                # Counter for correctly answered questions
    incorrectly_answered = []      # List to track questions answered incorrectly
    
    for question in questions:
        # Check if the current question has been answered correctly already
        if not question.correct:
            # Prompt the user for an answer to the question
            user_answer = input(f"What is {question.string}?: ")

            # Check if the user's answer is correct
            if user_answer == str(question.answer):
                # Mark the question as correctly answered
                question.correct = True
                num_correct += 1
            else:
                # Add the question to the list of incorrectly answered questions
                incorrectly_answered.append(question)
                question.attempts += 1

            # Provide feedback if practice mode is enabled
            if practice:
                if question.correct:
                    print("Correct!")
                else:
                    if question.attempts == 3:
                        # After 3 incorrect attempts, provide the correct answer
                        print(f"You got this wrong too many times. The correct answer is {question.answer}.")
                    else:
                        # Provide feedback on the incorrect answer
                        print(f"Incorrect. The correct answer is {question.answer}.")
                    question.attempts += 1
                    question.correct = False

    # Return the count of correct answers and the list of incorrectly answered questions
    return num_correct, incorrectly_answered
