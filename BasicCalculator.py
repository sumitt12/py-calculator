def add(a, b):
    print(a + b)

def subtract(a, b):
    print(a - b)

def multiply(a, b):
    print(a * b)

def divide(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("Cannot divide by O.")

def modulus(a, b):
    try:
        print(a % b)
    except ZeroDivisionError:
        print("Cannot divide by O.")

while True:
    print("Welcome to Basic Calculator")
    print("Choose an operation:")
    print("Addition")
    print("Subtraction")
    print("Multiplication")
    print("Division")
    print("Modulus")
    try:
        calculate = str(input("Enter your choice: "))
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        match calculate:
            case "addition"|"add":
                add(a,b)
            case "subtraction"|"sub":
                subtract(a,b)
            case "multiplication"|"multiply":
                multiply(a,b)
            case "division"|"divide":
                divide(a,b)
            case "modulus"|"mod":
                modulus(a,b)
            case _:
                print("Invalid choice")
                print("Please try again.")
    except BaseException:
        print("An error occurred.")
    ch=input("Do you want to continue? (y/n): ")
    if ch == 'n' or ch == 'N':
        break

            
