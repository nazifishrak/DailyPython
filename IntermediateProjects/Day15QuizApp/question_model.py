class Question:
    """
    Represents a question that has a question text and the correct answer
    """

    def __init__(self, text: str, answer: str) -> None:
        self.question = text
        self.answer = answer
    
