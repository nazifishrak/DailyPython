from typing import List
from quiz_brain import QuizBrain
from question_model import Question
from data import question_data

question_bank: List[Question] = [] #Shows a list of Questions List<Question> 
for question in question_data:
    question_obj = Question(question['text'], question['answer'])
    question_bank.append(question_obj)

qb = QuizBrain(question_bank)
qb.next_question()
