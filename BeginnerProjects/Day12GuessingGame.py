import random


def guessing_game():
    """
    Starts the Guessing Game Application
    """
    continue_loop = True
    lives = 0
    random_number = random.randint(1,100)
    #Chooses diffulty level and assigns the number of lives based on that
    while continue_loop:
        level = input("Choose difficulty level by typing easy/hard: ")

        if level == "easy":
            lives = 10
            continue_loop = False
        elif level == "hard":
            lives = 5
            continue_loop = False
        else:
            print("invalid input")
            continue_loop = True

  # Continues asking the user for a number if thne answer is not the computer's number till it has life  

    while lives>0:
        user_inp = int(input("Guess a number between 1 and 100: "))
        if user_inp>random_number:
            print("The number is too high")
            lives -=1
            print(f"You has {lives} lives remaining")
        elif user_inp<random_number:
            print("The number is too low")
            lives -=1
            print(f"You has {lives} lives remaining")
        else:
            print("Yay! You guessed it right")
            print(f"The correct answer was {random_number}")
            break

    if lives<=0:
        print("You are out of tries! 😟")
        print(f"The correct answer was {random_number}")
    
    if input("Do you want to play again y/n: ") == "y":
        guessing_game()
    else:
        pass

guessing_game()
