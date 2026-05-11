class Dog:
    species = "Canis lupus familiaris"

    def __init__(self, name, breed, age):
        self.name  = name
        self.breed = breed
        self.age   = age

    def bark(self):
        return f"{self.name} says: Woof!"

    def human_years(self):
        return self.age * 7

    def __str__(self):
        return f"{self.name} ({self.breed}), {self.age} yrs"

d1 = Dog("Bruno", "Labrador", 3)
d2 = Dog("Max",   "Pug",      5)

pran_years())
print(d2.age)

class Car:
    def __init__(self, name, speed, fuel):   
        self.name  = name                  
        self.speed = speed
        self.fuel  = fuel

    def describe(self):
        print(self.name, self.speed)

my_car = Car("Tesla", 250, "electric")
my_car.describe()
print(my_car.fuel) 

class Counter:
    total = 0

    def __init__(self, name):
        self.name  = name
        self.count = 0

    def click(self):
        self.count   += 1
        Counter.total += 1

    def __str__(self):
        return f"{self.name}: {self.count} (global: {Counter.total})"

a = Counter("A")
b = Counter("B")
a.click()
a.click()
b.click()
print(a)
print(b)
print(Counter.total)

class Bankaccount:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self,amount):
        selfint(d1.bark())
print(d2.human_years())
print(d1.species)
print(d2)
d1.age = 4
print(d1.hum.balance += amount
        print("Balance : ",self.balance)

    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance -=amount
            print("Balance : ",self.balance)
        else:
            print("Insufficient balance")

    def __str__(self):
       return f"Owner: {self.owner} | Balance: ₹{self.balance}"


acc = Bankaccount("Aarush",5000)
acc.deposit(20000)
acc.withdraw(2000)
print(acc)

class student:
    def __init__(self,name,marks,age,grade):
        self.name = name
        self.marks = marks
        self.age = age
        self.grade = grade
        self.avg = sum(marks)/len(marks)

    def compare(self,other):
        if self.avg > other.avg:
            print(f"{self.name} has a higher average: {self.avg} vs {other.avg}")
        elif self.avg < other.avg:
            print(f"{other.name} has a higher average: {other.avg} vs {self.avg}")
        else:
            print("It's a tie!")

Aarush = student("Aarush", [85, 90, 83],12,8)
Vihaan = student("Vihaan", [92, 94, 93],12,8)
Advik =  student("Advik", [70, 72, 72],12,8)

Aarush.compare(Vihaan)
Aarush.compare(Advik)

class book:
    def __init__(self,title,author,pages,ratings):
        self.title = title
        self.author = author
        self.pages = pages
        self.ratings = ratings
    
    def summary(self):
        print("The details are : ",self.title, self.author, self.pages, self.ratings)
    
    def is_long(self):
        return self.pages>300

    def __str__(self):
        return f"{self.title} by {self.author}"

b = book("Harry Potter","Jk Rowling",450,8.7)
b.summary()
print(b.is_long())
print(b)
