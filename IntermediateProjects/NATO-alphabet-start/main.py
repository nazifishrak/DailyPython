
import pandas
student_data_frame = pandas.read_csv('./nato_phonetic_alphabet.csv')

new_dict = {row.letter: row.code for (index, row) in student_data_frame.iterrows()}
print(new_dict)

