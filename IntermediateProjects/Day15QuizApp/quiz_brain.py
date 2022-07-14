from pydoc import importfile
from typing import List

from question_model import Question
from os import system

class QuizBrain:
    """
    Controls the logic of how the quiz works
    ****Functions you can use: ****
    next_question(), has_next_questions()
    check_answer()

    Fields: 
    question_number
    q_list --> List of Questions


    """
    def __init__(self, q_list: List[Question]) -> None:
        self.question_number = 0
        self.q_list = q_list
        self.score = 0


    def next_question(self) -> str:
        """
        Asks user the next question and returns their answer as a string
        """
        self.question_number += 1
        inp = input(f"Q{self.question_number}. {self.q_list[self.question_number-1].question} (Y/N)?")
        # system('cls') \\Uncomment if you want to clear previous questions from the console
        if inp.lower() == "y":
            return "True"
        else:
            return "False"
    
    def has_next_questions(self) -> bool:
        """
        Returns true if there are more questions left in the question bank
        """
        if self.question_number == len(self.q_list):
            return False
        else:
            return True
    
    def check_answer(self, ans: str) -> None:
        """
        Checks if the user's answer is rignt and updates the score accordingly
        """
        answer = self.q_list[self.question_number-1].answer
        if answer == ans:
            self.score +=1
            print(f"You got it right. Your current score is {self.score}/{self.question_number}")
            
            
        else:
            print(f"You got it wrong. Your current score is {self.score}/{self.question_number}")
        print(f"The correct answer was {answer}\n")

            
        