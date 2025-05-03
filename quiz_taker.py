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
    a = lines[2][3:].strip()
    b = lines[3][3:].strip()
    c = lines[4][3:].strip()
    d = lines[5][3:].strip()
    correct = lines[6].split(":")[1].strip().lower()

    question_data = {
        'question': question_line,
        'choices': {'a': a, 'b': b, 'c': c, 'd': d},
        'correct': correct
    }

    questions.append(question_data)

# Shuffle the questions to randomize the order
# Loop through questions and ask for the user's answers
# Validate if answers are correct
# Show the final score