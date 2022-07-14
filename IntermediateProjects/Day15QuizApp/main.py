from typing import List
from quiz_brain import QuizBrain
from question_model import Question
from data import question_data
from os import system
question_bank: List[Question] = [] #Shows a list of Questions List<Question> 
for question in question_data:
    question_obj = Question(question['text'], question['answer'])
    question_bank.append(question_obj)
    """
    Builds a question bank from the given data
    """



qb = QuizBrain(question_bank)
while qb.has_next_questions():
    qb.check_answer(qb.next_question())

    


