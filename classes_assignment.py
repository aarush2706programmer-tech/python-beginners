class Student1:
    school = 'DPS Pune'
 
    def __init__(self, name, age):
        self.name = name
        self.age  = age
 
    def greet(self):
        print(f'Hi, I am {self.name}, age {self.age}')
 
s1 = Student1('Aryan', 13)
s2 = Student1('Priya', 14)
s1.greet()
s2.greet()
print(Student1.school)
print(s1.name == s2.name)


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner   = owner
        self.balance = balance
 
    def deposit(self, amount):
        self.balance += amount
        print(f'Deposited {amount}. Balance: {self.balance}')
 
    def __str__(self):
        return f'{self.owner}: Rs.{self.balance}'
 
acc = BankAccount('Aryan')
acc.deposit(500)
print(acc)


class Book:
    def __init__(self, title, author, pages):
        self.title  = title
        self.author = author
        self.pages  = pages

    def summary(self):
        print(f'"{self.title}" is a book by {self.author} with {self.pages} pages.')
 
    def __str__(self):
        return f'"{self.title}" by {self.author} with {self.pages} pages.'


class Student1:
    def __init__(self, name):
        self.name  = name
        self.marks = []
 
    def add_mark(self, score):
        self.marks.append(score)
 
    def average(self):
        if not self.marks:
            return 0
        return round(sum(self.marks) / len(self.marks), 1)
 
    def is_passing(self, pass_mark=40):
        return self.average() >= pass_mark
 
s = Student1('Aryan')
s.add_mark(70)
s.add_mark(80)
print(s.is_passing())   


student = {"name": "Aryan", "age": 13, "marks": 70}
print("grade" in student)



#Assinment 2

student = {"name": "Priya", "age": 14, "grade": "8th"}
print(student["name"])
print(student.get("age"))
print(student.get("phone", "Not found"))
print(len(student))

scores = {"Maths": 80, "Science": 75}
scores["English"] = 90
scores["Maths"]   = 95
del scores["Science"]
print(scores)
print(len(scores))

marks = {"Maths": 88, "Science": 92, "English": 79}
for subject, score in marks.items():
    print(f"{subject}: {score}")

book = {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "pages": 180, "genre": "Fiction"}
print(book["title"])
print(len(book))
print("price" in book)

marks = {"Maths": 88, "Science": 72, "English": 95, "History": 65, "Art": 80}
for i,j in marks.items():
    print(f"{i}: {j}")
print(sum(marks.values()))
print(round(sum(marks.values())/len(marks), 2))
print(len(marks))

classroom = {
    "student1": {
        "age": 13,
        "grade": "8th",
        "favourite_subject": "Maths"
    },
    "student2": {
        "age": 14,
        "grade": "9th",
        "favourite_subject": "Science"
    }
}
print(classroom["student1"]["age"])
print(classroom["student2"]["favourite_subject"])
classroom["student1"]["score"] = 90
print(classroom["student1"])


#Assignment 3
word = "  Python  "
print(word.strip())
print(word.strip().upper())
print(len(word.strip()))

msg = "Hello World"
print(msg[0])
print(msg[-1])
print(msg[6:11])
print(msg[:5])

name = "Aarush"
age = 12
favorite_subject = "Maths"
print(f"My name is {name}, I am {age} years old and my favorite subject is {favorite_subject}.")
print(name.upper())
print(len(name))

sentence = "the quick brown fox"
print(sentence.title())
print(sentence[0:10])
print(sentence[::-1])
print(len(sentence))
print(sentence[16:19])
