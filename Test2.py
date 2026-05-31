#Q19
name = 'Aryan'
age  = 13
tall = True
print(name)
print('Age:', age)
print('Is tall?', tall)
marks = 82
if marks >= 90:
    print('Grade: A')
elif marks >= 75:
    print('Grade: B')
else:
    print('Grade: C')


#Q20
for i in range(1, 4):
    print('Step', i)
 
count = 3
while count > 0:
    print(count)
    count = count - 1
print('Done!')


#Q21
def greet(name, greeting='Hello'):
    print(greeting + ', ' + name + '!')
 
fruits = ['apple', 'banana', 'mango']
fruits.append('grapes')
print(len(fruits))
print(fruits[0])
print(fruits[-1])
greet('Aryan')


#Q20
player = {
    'name':   'Aryan',
    'level':  5,
    'health': 100,
}
player['health'] = 80
player['score']  = 250
print(player.get('health'))
print(player.get('gold', 0))
print('level' in player)
for key, value in player.items():
    print(key, '->', value)


#Q23
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age  = age
    def eat(self):
        print(self.name + ' is eating.')
    def __str__(self):
        return self.name + ' (age ' + str(self.age) + ')'
 
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    def bark(self):
        print(self.name + ' says: Woof!')
    def __str__(self):
        return self.name + ' the ' + self.breed
d = Dog('Bruno', 3, 'Labrador')
d.eat()
d.bark()
print(d)
print(isinstance(d, Animal))
print(d.age)


#Q24
score = int(input('Enter score: '))
if score >= 90:
    print('Grade: A')

#Q25
class Student:
    def __init__(self,name, age):     # BUG
        self.name = name
        self.age  = age

#Q26
def is_valid_buggy(s):
    stack = stack()
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in '([':
            stack.push(char)
        elif char in ')]}':
            if stack.peek() or stack.is_empty() != pairs[char]:  # BUG
                return False
            stack.pop()
    return stack.is_empty()

#Q27
num = [1,2,3,4,5]
for i in num:
    print(i)
    if i/2==0:
        print("This is even")
    else:
        print("This is odd")
print(min(num))
print(max(num))

total = 0
for i in range(1, 6):
    total = total + i
print("Total:", total)

def add_ten(n):
    result = n + 10
    return result

answer = add_ten(5)
print("Answer:", answer)

scores = {"Aryan": 88, "Priya": 92, "Dev": 74}

for name,score in scores.items():
    print(name, "scored", score)

