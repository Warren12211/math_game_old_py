# Imports the random module to generate random numbers
import random

# Function to generate a set of questions based on the operation type, max integer value, and number of questions
def question_set_generator(op, max_int, num_questions):

    # Defines a Question class to hold the question string, correct answer, 
    # number of attempts made by the user, and whether the question has been answered correctly
    class Question():
        def __init__(self, string, answer):
            self.string = string          # The string representation of the question (e.g., "2 + 3")
            self.answer = answer          # The correct answer to the question (e.g., 5)
            self.attempts = 0             # Initialize the number of attempts to 0
            self.correct = False          # Initialize the correct flag to False (question not yet answered correctly)
        
        # String representation of the Question object, useful for debugging or displaying the question details
        def __str__(self):
            return f"Question: {self.string}, Answer: {self.answer}, Attempts: {self.attempts}"

    # Initialize some empty placeholder lists (not used in the final code)
    question_names = []
    question_strings = []
    question_answers = []
    question_list = []  # List to hold the generated Question objects

    # Use a match statement to determine the operation type
    # In this case, we are only handling addition ("add")
    match op:
        case "add":
            
            # Initialize a list to track generated question strings to avoid duplicates
            q_str_list = []
            i = 0  # Initialize a counter for the number of questions generated

            # Loop until the desired number of questions is generated
            while i < num_questions:
                # Generate two random integers between 1 and the maximum integer value
                num_1 = random.randint(1, max_int)
                num_2 = random.randint(1, max_int)

                # Create a string representing the question (e.g., "2 + 3")
                q_str = f"{num_1} + {num_2}"

                # Check if the question string has not been generated before
                if q_str not in q_str_list:
                    # Add the question string to the list of generated strings
                    q_str_list.append(q_str)
                    # Create a Question object with the string and the correct answer, then add it to the question list
                    question_list.append(Question(q_str, (num_1 + num_2)))
                    # Increment the counter since a unique question was generated
                    i += 1
                else:
                    # If the question string is a duplicate, continue to the next iteration without incrementing the counter
                    continue

    # Return the list of generated Question objects
    return question_list
