# Generates a list of Question objects
# op param selects which operation to use (e.g., "add" for addition)
# max_int determines the highest integer value used in the questions
# num_questions specifies how many questions to generate
import random

def question_set_generator(op, max_int, num_questions):
    # Defines a class to represent a question with its details
    class Question():
        def __init__(self, string, answer):
            self.string = string    # The question as a string (e.g., "5 + 3")
            self.answer = answer    # The correct answer to the question
            self.attempts = 0       # Tracks how many times the user has attempted this question
            self.correct = False    # Flag to check if the question has been answered correctly

        def __str__(self):
            # Return a string representation of the Question object
            return f"Question: {self.string}, Answer: {self.answer}, Attempts: {self.attempts}"

    # List to store all generated Question objects
    question_list = []

    # Generate questions based on the specified operation
    match op:
        case "add":
            q_str_list = []  # List to ensure all question strings are unique
            i = 0
            while i < num_questions:
                # Generate two random integers between 1 and max_int
                num_1 = random.randint(1, max_int)
                num_2 = random.randint(1, max_int)
                # Create a question string for addition
                q_str = f"{num_1} + {num_2}"

                # Check if this question string has already been used
                if q_str not in q_str_list:
                    # Add the question string to the list of used questions
                    q_str_list.append(q_str)
                    # Create a Question object and add it to the question_list
                    question_list.append(Question(q_str, num_1 + num_2))
                    i += 1  # Increment the counter to keep track of the number of questions created
                else:
                    # If the question string is a duplicate, continue to the next iteration
                    continue

    # Return the list of generated Question objects
    return question_list
