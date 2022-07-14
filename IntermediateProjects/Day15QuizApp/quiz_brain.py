from typing import List

from question_model import Question


class QuizBrain:
    def __init__(self, q_list: List[Question]) -> None:
        self.question_number = 0
        self.q_list = q_list


    def next_question(self) -> str:
        self.question_number += 1
        inp = input(f"Q{self.question_number}. {self.q_list[self.question_number-1].question} (Y/N)?")