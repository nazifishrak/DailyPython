# Automated writing letters for different people 

PLACEHOLDER = "[name]"
with open("./Input/Names/invited_names.txt") as name_list:
    name_list = name_list.readlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    letter_content = letter.read()

    for name in name_list:
        new_letter=letter_content.replace(PLACEHOLDER, name.strip())
        with open(f'./Output/ReadyToSend/letter_for_{name.strip()}', 'w') as write_letter:
            write_letter.write(new_letter)
