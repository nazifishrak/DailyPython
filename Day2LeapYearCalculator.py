
year = int(input("Which year do you want to check? "))

if year%4==0:
    if year%100==0:
        if year%400==0:
            print("Leap")
        else:
            print("Not Leap")
    else:
        print("Leap")
else:
    print("Not Leap")
