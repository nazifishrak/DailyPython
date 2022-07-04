#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip Calculator")
bill= float(input("What was the total bill $ "))
TIP_PERCENTAGE = float(input("What percentage would you like to tip "))
NO_OF_PEOPLE = int(input("Between how many people would the bill be split "))

total_payable = bill*TIP_PERCENTAGE/100 + bill
# formats the number to a 2dp floating point and prints it with a f string
print(f"Each person will pay {'{:.2f}'.format((total_payable/NO_OF_PEOPLE))}")


