inp = int(input("Check this number: "))

def prime_checker(number = inp) -> None:
    for i in range(2,number+1):
        if number%i==0 and (not(number == i)):
            print("Not Prime")
            break
        else:
            if (i==number):
                print("prime")

        
prime_checker()