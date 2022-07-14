
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1= name1.lower()
name2= name2.lower()
combinedName = name1+name2

TRUE = combinedName.count("t") + combinedName.count("r")+ combinedName.count("u")+combinedName.count("e")
LOVE = combinedName.count("l")+combinedName.count("o")+combinedName.count("v")+combinedName.count("e")
result = int(str(TRUE)+str(LOVE))

if result<10 or result>90:
    print(f"Your score is {result}, you go together like coke and mentos.")
elif result>40 and result<50:
    print(f"Your score is {result}, you are alright together.")
else:
    print(f"your result is {result}")
