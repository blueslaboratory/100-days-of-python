# 21/02/2024
# Day - 017



##################################################
# DAY 17 PROJECT: QUIZ BRAIN

print("\n*** Welcome to the Quiz Brain ***")

from question_model import Question
from data import question_dataset_2
from quiz_brain import QuizBrain

question_bank = []


for q in question_dataset_2:
    
    text = q["question"]
    answer = q["correct_answer"]
    
    question_object = Question(text, answer)
    question_bank.append(question_object)
    
    
# printing all the objects
# print(question_bank)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    
    
print("\nYou've completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}")