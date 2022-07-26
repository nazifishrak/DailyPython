
from typing import List
import pandas
student_data_frame = pandas.read_csv('./nato_phonetic_alphabet.csv')

nato_alphabet_dict = {row.letter: row.code for (index, row) in student_data_frame.iterrows()}


user_input = input("Enter a word: ")

def split_letters(word: str) -> List[str]:
    """Returns a list of letters that are present in a word"""
    if word == "":
        return []
    else:
        return [word[0]] + split_letters(word[1::])

result = [nato_alphabet_dict[letter.upper()] for letter in split_letters(user_input)]
print(f"The NATO phoenetic alphabets are  ")
print(result)