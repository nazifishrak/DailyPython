inp = int(input("Check this number: "))

def prime_checker(number = inp) -> None:
    for i in range(2,number+1):
        if number%i==0 and (not(number == i)):
            print(f"The number {number} is Composite")
            break
        else:
            if (i==number):
                print(f"The number {number} is Prime")

def prime_checker_alternate(number = inp) -> None:
    is_prime = True
    for i in range(2,number):
        if number % i ==0:
            is_prime = False
    if is_prime:
        print(f"The number {number} is Prime")
    else:
        print(f"The number {number} is Composite")

        
# prime_checker()
prime_checker_alternate()