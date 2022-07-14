rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

from random import randint as randint
moves=[rock,paper,scissors]
random_number = randint(0,2)
inp = int(input("Choose 0 for rock, 1 for paper, 2 for scissor: "))
print(f"You chose {moves[inp]}")
print(f"Computer chose {moves[random_number]}")

if inp == random_number:
    print("Tie")
elif inp==0 and random_number == 1:
    print("Computer won")

elif inp==1 and random_number == 2:
    print("Computer won")

elif inp==2 and random_number == 0:
    print("Computer won")

else:
    print("You won")

