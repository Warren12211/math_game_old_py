def AskQuestions(questions, practice=False):
    # Loop through each question in the list
    for i in range(len(questions)):
        # Check if the question has not been answered correctly
        if questions[i].correct == False:
            # Ask the user to answer the question
            user_answer = input(f"What is {questions[i].string}?: ")

            # If the user's answer is correct, mark the question as answered correctly
            # and increase the global count of correct answers
            if user_answer == str(questions[i].answer):
                questions[i].correct = True  # Mark the question as answered correctly
                global num_correct
                num_correct += 1  # Increment the count of correct answers
            # If the user's answer is incorrect, increment the attempts counter
            else:
                questions[i].attempts += 1  # Increase the attempt count for this question

            # If the practice mode is True, provide additional feedback
            if practice == True:
                # If the answer is correct during practice, confirm that
                if questions[i].correct == True:
                    print("Correct!")  # Inform the user that the answer is correct
                    questions[i].correct = True  # Mark the question as correct
                # If the answer is incorrect during practice, provide feedback
                else:
                    # If the user has made 3 incorrect attempts, show the correct answer
                    if questions[i].attempts == 3:
                        print(f"You got this wrong too many times. The correct answer is {questions[i].answer}.")
                    else:
                        # Tell the user that the answer is incorrect and show the correct answer
                        print(f"Incorrect. The correct answer is {questions[i].answer}.")
                    questions[i].attempts += 1  # Increment the attempts counter
                    questions[i].correct = False  # Ensure the question remains marked as incorrect


def GiveResults(num_correct, incorrectly_answered):
    # Determine the appropriate word ("question" or "questions") based on the number of correct answers
    if num_correct == 1:
        question_string = "question"  # Singular if only one question was answered correctly
    else:
        question_string = "questions"  # Plural if more than one question was answered correctly

    # Print the number of correctly answered questions
    print(f"\nYou got {num_correct} {question_string} right!")

    # Determine the appropriate word ("question" or "questions") based on the number of incorrect answers
    if len(incorrectly_answered) == 1:
        question_string = "question"  # Singular if only one question was answered incorrectly
    else:
        question_string = "questions"  # Plural if more than one question was answered incorrectly

    # Print the number of incorrectly answered questions
    print(f"You got {len(incorrectly_answered)} {question_string} wrong.")