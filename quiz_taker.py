import random
import pyfiglet
from colorama import Fore, Style, init
init(autoreset=True)

banner = pyfiglet.figlet_format("QUIZ TIME")
print(Fore.CYAN + banner)
# Open and read the file
with open("questions_for_quiz.txt", "r") as file:
    content = file.read().strip()
# Split the file content by question to separate each question block
question_blocks = content.split("Question")[1:]
# Organize the questions
questions = []

for block in question_blocks:
    lines = block.strip().split("\n")
    
    question_line = lines[1].replace("Question: ", "").strip()
    choice_a = lines[2][3:].strip()
    choice_b = lines[3][3:].strip()
    choice_c = lines[4][3:].strip()
    choice_d = lines[5][3:].strip()
    correct = lines[6].split(":")[1].strip().lower()

    question_data = {
        'question': question_line,
        'choices': {'a': choice_a, 'b': choice_b, 'c': choice_c, 'd': choice_d},
        'correct': correct
    }

    questions.append(question_data)
# Shuffle the questions to randomize the order
random.shuffle(questions)
# Loop through questions and ask for the user's answers
score = 0
total = len(questions)

for question_index, question_data in enumerate(questions, start=1):
    print(f"\nQuestion {question_index}: {question_data['question']}")
    print("a:", question_data['choices']['a'])
    print("b:", question_data['choices']['b'])
    print("c:", question_data['choices']['c'])
    print("d:", question_data['choices']['d'])

    answer = input("Your answer (a/b/c/d): ").lower()
    
    while answer not in ['a', 'b', 'c', 'd']:
        answer = input("Invalid. Please type a, b, c, or d: ").lower()
# Validate if answers are correct
    if answer == question_data['correct']:
            print("Correct!")
            score += 1
    else:
        print(f"Wrong. Correct answer is {question_data['correct']}")
# Show the final score
print(f"\nYour final score: {score}/{total}")
percent = (score / total) * 100
print(f"That's {percent:.2f}% correct!")