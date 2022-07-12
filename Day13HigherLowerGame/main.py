import random
from unicodedata import name
from game_data import data
import ascii_art

score = 0
game_not_over = True
def question_builder(data1: dict,data2: dict) -> None:

    print(f"Compare A: {data1['name']}, a {data1['description']} from {data1['country']}")

    print(f"""
    {ascii_art.vs}""")

    print(f"Compare B: {data2['name']}, a {data2['description']} from {data2['country']}")    

def compare(inp: str, data1: dict, data2: dict):
    global score
    global game_not_over
    if inp=="A" and data1['follower_count'] >= data2['follower_count']:
        score +=1
        print(f"You're right! current score: {score}")
        game_not_over = True
    elif inp =="B" and data1['follower_count'] <= data2['follower_count']:
        score +=1
        print(f"You're right! current score: {score}")
        game_not_over = True
    else: 
        print(f"You lose! Final Score: {score}")
        game_not_over = False


while game_not_over:
    random_data_dict1 = random.choice(data)
    random_data_dict2 = random.choice(data)
    question_builder(random_data_dict1, random_data_dict2)
    inp = input("Who has more followers, type 'A' or 'B': ")
    
    compare(inp, random_data_dict1, random_data_dict2)
        



