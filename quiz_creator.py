# Ask the user a question
while True:
    question = input("Enter a question: ")
# Ask the user for an answer and the correct answer
    choice_a = input("Enter the answer as choice a: ")
    choice_b = input("Enter the answer as choice b: ")
    choice_c = input("Enter the answer as choice c: ")
    choice_d = input("Enter the answer as choice d: ")
    
    correct_answer = input("Enter which of the choices is the correct answer: ").lower()
    
# Validate the correct answer
    while correct_answer not in ["a", "b", "c", "d"]:
        correct_answer = input("Please enter a valid and correct answer: ").lower()
# Loop until the user wants to exit the program
# Append and save questions and answers to a file 
# Break loop if user wants to exit
    with open("questions_for_quiz.txt", "a") as file:
        file.write("Question: " + question + "\n")
        file.write("a: " + choice_a + "\n")
        file.write("b: " + choice_b + "\n")
        file.write("c: " + choice_c + "\n")
        file.write("d: " + choice_d + "\n")
        file.write("Correct Answer: " + correct_answer + "\n")
        file.write("     \n\n")
        
        additional_questions = input("Do you want to add more questions?: ").lower()
        if additional_questions == "no":
            break