# Generates a list of Question objects
# Op param selects which operation
# top_num is what the highest number in the set will be:
# top_num 10, last question will be 10 + 10, top_num 5, last question will be 5 + 5
# list_name is the name of the returned list of questions


def question_set_generator(op, top_num):

    # Defines a question class that saves the question string, answer, and status
    class Question():
        def __init__(self, string, answer, status):
            self.string = string
            self.answer = answer
            self.status = status

        def __str__(self):
            return f"Question: {self.string}, Answer: {self.answer}, Status: {self.status}"

           

    # Some empty placeholder lists
    question_names = []
    question_strings = []
    question_answers = []
    question_list = []

    # If op == "add", run some stuff
    match op:
        case "add":

            # Adds a question name (a1_1), string (1 + 1), and answer (2) to
            # separate lists
            for num1 in range(1, top_num + 1):
                num2 = 0
                for j in range(top_num):
                    num2 += 1
                    question_names.append(f"a{num1}_{num2}")
                    question_strings.append(f"{num1} + {num2}")
                    question_answers.append(f"{num1 + num2}")

            # For each item in the list, create a object
            for i in range(len(question_names)):
                question_names[i] = Question(question_strings[i], question_answers[i], "unanswered")
                question_list.append(question_names[i])

    return question_list





 




                    