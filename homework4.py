def square(n):
    return n * n

def add_one(n):
    return n + 1

def describe(n):
    sq = square(n)
    result = add_one(sq)
    return f"{n} squared plus one = {result}"

print(describe(4))#This prints - 4 squared plus one = 17
print(describe(7))#This prints - 7 squared plus one = 50

def double(n):
    #print(n * 2)         line A 
    return(n*2)

def triple_then_double(n):
    tripled = n * 3
    return double(tripled)

result = triple_then_double(5)
print("Result:", result)

def metres_to_cm(f):
    return f * 100

def cm_to_inches(cm):
    return cm * 0.3937

def convert_all(m):
    cm = metres_to_cm(m)
    inches = cm_to_inches(cm)
    print(f"{m} metres = {cm} cm = {round(inches, 2)} inches")

convert_all(2)

import math
print(math.sqrt(225))
print(math.ceil(9.1))
print(math.floor(9.9))
print(round(math.pi, 3))
print(math.factorial(4))


import random
nums = random.sample(range(1, 51), 10)
random.shuffle(nums)
chosen = random.sample(nums, 3)
print("List:", nums)
print("Chosen:", chosen)
print("Sum:", sum(chosen))

# Original — crashes on bad input
try:
    a = int(input("First number: "))
    b = int(input("Second number: "))
    print(a / b)
except ZeroDivisionError:
    print("Division be zero is not allowed")
except ValueError:
    print("Please enter a integer")

def get_positive_number():
    while True:
        try:
            num = int(input("Enter a number"))
            if num < 0:
                print("Enter a positive number")
            else:
                print("You entered a positive number")
                break
        except ValueError:
            print("Invalid input")
get_positive_number()

import random

questions = {
    "2 + 2": "4",
    "5 x 6": "30",
    "10 - 3": "7",
    "9 / 3": "3",
    "7 + 8": "15"
}

selected = random.sample(list(questions.items()), 3)

score = 0

for q, ans in selected:
    try:
        user = input(q + ": ")
        if user == ans:
            score += 1
            print("Good job")
    except:
        print("Error")

print("Score:", score, "/3")


