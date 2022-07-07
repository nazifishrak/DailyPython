from random import randint as randint
names = input("Give me everybody's name separated by  a space: ")
names = names.split(" ")
payer= names[randint(0,len(names))]
print(f"{payer} pays the bill")