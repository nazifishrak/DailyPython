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
def calculator():
    loop_on = True
    num1 = int(input("Enter the first number: "))
    while loop_on:
        
        num2 = int(input("Enter the next number: "))

        for key in operation_dict:
            print(key)
        operation = input("Choose from the above operations: ")
        answer = operation_dict[operation](num1,num2)


        print(f"Result: {num1} {operation} {num2} = {answer}")
        
        should_continue = input("Do you want to perform more operations? y/n: ")
        if should_continue == "n":
            loop_on = False
            print("Calculator is shutting down...")
            print("Goodbye!")
        elif should_continue == "y":
            num1 = answer
        else:
            loop_on = False
            calculator()

calculator()