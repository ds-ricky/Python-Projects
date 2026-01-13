import art

def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(art.logo)
    repeat = True
    first_no = float(input("Enter your first number: "))

    while repeat:
        for key in operations:
            print(key)
        choose = input("Choose operation to perform: ")
        second_no = float(input("Enter your second number: "))
        result = operations[choose](first_no, second_no)
        print(f"{first_no} {choose} {second_no} = {result}")

        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation, or exit from calculator type 'x': ")

        if choice == "y":
            first_no = result

        elif choice == "x":
            print("Thanks for using")
            repeat = False

        else:
            repeat = False
            print("\n" * 25)
            calculator()

calculator()