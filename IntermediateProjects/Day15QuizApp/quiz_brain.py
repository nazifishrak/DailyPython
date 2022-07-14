from typing import List

from question_model import Question


class QuizBrain:
    def __init__(self, q_list: List[Question]) -> None:
        self.question_number = 0
        self.q_list = q_list
        self.score = 0


    def next_question(self) -> str:
        self.question_number += 1
        inp = input(f"Q{self.question_number}. {self.q_list[self.question_number-1].question} (Y/N)?")
        if inp.lower() == "y":
            return "True"
        else:
            return "False"
    
    def has_next_questions(self) -> bool:
        if self.question_number == len(self.q_list):
            return False
        else:
            return True
    
    def check_answer(self, ans: str) -> None:
        answer = self.q_list[self.question_number-1].answer
        if answer == ans:
            self.score +=1
            print(f"You got it right. Your current score is {self.score}/{self.question_number}")
        else:
            print(f"You got it wrong. Your current score is {self.score}/{self.question_number}")
        print(f"The correct answer was {answer}")

            
        