from audioop import mul


def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mult(a,b):
    return a * b
def div(a,b):
    return a / b
operation_dict = {
    "+" : add,
    "-" : sub,
    "*" : mult,
    "/" : div
}
loop_on = True
while loop_on:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    for key in operation_dict:
        print(key)
    operation = input("Choose from the above operations: ")


    print(f"Result: {num1} {operation} {num2} = {operation_dict[operation](num1,num2)}")
    
    should_continue = input("Do you want to perform more operations? y/n: ")
    if should_continue == "n":
        loop_on = False
        print("Calculator is shutting down...")
        print("Goodbye!")
         