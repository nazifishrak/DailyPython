import asciiiArt
import wordList
import random
import re
state = True 
print(asciiiArt.logo)
# 
random_word = random.choice(wordList.word_list)
random_word_list=list(random_word)
# Creates a blank string to start with
blanks = ["_" for x in range(len(random_word))]

def listToString(listOfString):
    temp_string = ""
    for i in listOfString:
        temp_string += i
    return temp_string

def place_letters(letter,listOfPos):
    """
    places letter in the given position of the field blanks
    """
    for i in listOfPos:
        blanks[i]=letter

while len(asciiiArt.stages) and state >0 :
    tempList = []
    temp_random_list = random_word_list.copy()
    user_letter = input("Guess a letter\n")
    if user_letter in random_word_list:

        tempList = [i.start() for i in re.finditer(user_letter, random_word)]
        place_letters(user_letter,tempList)
        print(listToString(blanks))
        if listToString(blanks) == random_word:
            print("YOU WON!!!")

            break
    else:
        print(asciiiArt.stages[-1])
        asciiiArt.stages.pop(-1)
        if len(asciiiArt.stages)==0:
            print(asciiiArt.game_over) 
    
print("The Word was", random_word)        
    
        




