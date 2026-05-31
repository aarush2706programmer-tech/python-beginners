name = input("What is your name")
age = int(input("How old are you: "))
next_year = age + 1
if age > 12:
    print("Hello,", name)

marks = int(input("Your marks: ")) # user types: 88
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
else:
    print("Grade: C")
#If user types 91
#Then output will be A

count = 1
while count <= 5:
    print("Count is", count)
    count = count + 1
print("Done!")

num = 9
for i in range(1,11):
    print("9 x",i,"=",num*i)

scores = [85, 92, 78, 95, 60]
scores.append(88)
print(len(scores))
print(max(scores))
print(min(scores))
print(scores[0])
print(scores[-1])

def square(n):
    return n * n 
result = square(5)
print("5 squared is", result)

def ask_question(question,answer):
    user_answer = int(input("How many letters are there in the alphabet"))
    if user_answer == answer:
        print("You are correct")
    else:
        print("You are wrong")
ask_question("How many letters are there in the alphabet",26)

player = {
"name": "Aryan",
"level": 5,
"health": 100,
}
player["health"] = 80
player["score"] = 250
del player["level"]
print(player.get("score"))
print(player.get("gold", 0))
print("name" in player)
for key, value in player.items():
    print(key, "=", value)

students = {
    "Aryan": {"age": 13, "score": 92, "city": "Pune"},
    "Priya": {"age": 13, "score": 88, "city": "Mumbai"},
}
print(students["Aryan"]["score"])
print(students["Priya"]["city"])
for i,j in students.items():
    print(i,j)

class Student:
    school = "DPS Pune"
    def __init__(self, name, age):
        self.name = name
        self.age  = age
    def __str__(self):
        return f"Student: {self.name}, Age: {self.age}"
    def __len__(self):
        return self.age 
aryan = Student("Aryan", 13)
priya = Student("Priya", 13)
aryan.age = 14
print(aryan)
print(priya.age)
print(aryan.school)
print(len(aryan))
print(isinstance(aryan, Student))

class Animal:
    def __init__(self, name, age):
        self.name = name

        self.age  = age
    def eat(self):
        print(f"{self.name} is eating.")
    def __str__(self):
        return f"{self.name} (age {self.age})"
 
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    def bark(self):
        print(f"{self.name} says: Woof!")
    def __str__(self):
        return f"{self.name} the {self.breed} (age {self.age})"
 
d = Dog("Bruno", 3, "Labrador")
d.eat()
d.bark()
print(d)
print(isinstance(d, Animal))


class Cat(Animal):
    def __init__(self, name, age, indoor):
        super().__init__(name, age)
        self.indoor = indoor
    def meow(self):
        location = 'indoor' if self.indoor else 'outdoor'
        print(f"{self.name} says: Meow!")


def get_first(lst):            # Big O: __1___
    return lst[0]
 
def find_max(lst):             # Big O: ___n____
    best = lst[0]
    for n in lst:
        if n > best: best = n
    return best
 
def print_pairs(lst):          # Big O: _______
    for i in lst:
        for j in lst:
            print(i, j)
 
def binary_search(arr, target): # Big O: _______
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target: return mid
        elif arr[mid] < target: left = mid+1
        else: right = mid-1
    return -1


def has_duplicate(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j]:
                return True
    return False
#This is O(nsquare)

def find_duplicates(lst):
    seen = set()
    duplicates = set()
    
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    
    return list(duplicates)

# Example
nums = [1, 2, 3, 2, 4, 3, 5]
print(find_duplicates(nums))  # [2, 3]

"""Q10 
True
True
False

Q16
True
True
True"""



