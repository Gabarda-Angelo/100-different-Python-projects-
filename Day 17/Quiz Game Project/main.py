from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank =[]

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)

    question_bank.append(new_question)


print(question_bank[0].text)

quiz_brain = QuizBrain(question_bank)


while quiz_brain.still_has_questions():
    quiz_brain.next_question()



print("You've completed the quiz.")
total_score = quiz_brain.score
total_questions = len(quiz_brain.question_list)

print(f"Your final score was:{total_score}/{total_questions}")










