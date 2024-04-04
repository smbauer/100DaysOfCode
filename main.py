from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


# initialize the list of questions
question_bank = [Question(question["text"], question["answer"]) for question in question_data]

# initialize the quiz logic
quiz_brain = QuizBrain(question_bank)

# loop through all the questions
while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You've completed the quiz.")
print(f"Your final score is {quiz_brain.score}/{quiz_brain.question_number}")
