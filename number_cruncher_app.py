def get_number(num):
    while True:
        try:
            return int(num)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            num = input("Enter a number: ")

import math
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Denominator cannot be zero.")
    return a / b

def power(a, b):
    return math.pow(a, b)

def my_sqrt(a):
    if a < 0:
        raise ValueError("Input cannot be a negative number.")
    return math.sqrt(a)

def sumarise(a,b):
    print("Sum:", add(a, b))
    print("Difference:", subtract(a, b))
    print("Product:", multiply(a, b))
    
    print("Quotient:", divide(a, b))
    
    print("Power:", power(a, b))
    
    print("Square Root of a:", my_sqrt(a))
    print("Square Root of b:", my_sqrt(b))

def main():
    while True:
        print("Welcome to the Number Cruncher App!")
        print("1.Add, 2.Subtract, 3.Multiply, 4.Divide, 5.Power, 6.Square Root, 7.Summarise, 8.Exit")
        choice = input("Enter your choice: ")
        if choice == '8':
            print("Thank you for using the Number Cruncher App. Goodbye!")
            break
        elif choice in ['1', '2', '3', '4', '5', '7']:
            num1 = get_number(input("Enter the first number: "))
            num2 = get_number(input("Enter the second number: "))
            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                try:
                    print("Result:", divide(num1, num2))
                except ValueError as e:
                    print(e)
            elif choice == '5':
                print("Result:", power(num1, num2))
            elif choice == '7':
                sumarise(num1, num2)
        elif choice == '6':
            num = get_number(input("Enter a number: "))
            print("Result:", my_sqrt(num))
        else:
            print("Invalid choice. Please try again.")
main()