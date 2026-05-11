#Error Handling
try: 
    a = int(input("Enter a number: "))
    print("The number you entered is: ", a)
except ValueError:
    print("Invalid input. Please enter a valid number.")

try:
    b = int(input("Enter one number: "))
    c = int(input("Enter another number: "))
    result = b / c
    print("The result of division is: ", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")