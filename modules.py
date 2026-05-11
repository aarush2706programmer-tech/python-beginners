import math
print(math.sqrt(16))
print(math.pi)
print(math.floor(3.7))
print(math.factorial(5))
print(math.pow(2,2))
r = 5
a = round(math.pi*math.pow(r,2),2)
print(a)

import random
print(random.randint(1,10))
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
print(random.choice(names))
random.shuffle(names)
print(names)
print(random.sample(names, 3))

from datetime import datetime
now = datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)


print(now.strftime("%Y-%B-%d %H:%M:%S"))

birthdate = datetime(2013,6,27)
today = datetime.today()
age1=(today - birthdate).days
print("Age in days:", age1//365)
age = (today.year - birthdate.year)
print("Age in years:", age)

import os
print(os.getcwd())
print(os.listdir())
print(os.path.exists("day4.py"))

from math import sqrt, pi
print(sqrt(25))
print(pi)
