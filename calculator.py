#calculator
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def power(a, b):
    return a ** b

def modulus(a, b):
    return a % b

def floor_division(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a // b

def calculator():
    while True:
        print("Select operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power")
        print("6. Modulus")
        print("7. Floor Division ")
        print("8. Exit")

        choice = input("Enter choice (1/2/3/4/5/6/7/8): ")

        if choice == '8':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5', '6', '7']:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))

            if choice == '1':
                print(f"The result is: {addition(num1, num2)}")
            elif choice == '2':
                print(f"The result is: {subtraction(num1, num2)}")
            elif choice == '3':
                print(f"The result is: {multiplication(num1, num2)}")
            elif choice == '4':
                print(f"The result is: {division(num1, num2)}")
            elif choice == '5':
                print(f"The result is: {power(num1, num2)}")
            elif choice == '6':
                print(f"The result is: {modulus(num1, num2)}")
            elif choice == '7':
                print(f"The result is: {floor_division(num1, num2)}")
        else:
            print("Invalid input, please try again.")

calculator()
