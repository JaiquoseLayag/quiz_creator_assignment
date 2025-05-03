# Open and read the file
with open("questions_for_quiz.txt", "r") as file:
    content = file.read().strip()
# Split the file content by question to separate each question block
question_blocks = content.split("Question")[1:]
# Shuffle the questions to randomize the order
# Loop through questions and ask for the user's answers
# Validate if answers are correct
# Show the final score