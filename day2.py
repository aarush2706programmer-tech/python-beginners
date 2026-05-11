#STRING METHODS

name = "     Aarush     "
print(name)
print(name.strip())

a = "aarush"
print(a)
print(a.capitalize())
print(a.upper())

b="AARUSH"
print(b)
print(b.lower())

c="aarush singh"
print(c.title())

d = "my name is aarush singh, and i am 12 years old. i live in delhi, and my mobile number is 1234567890 and i study in MSPA"
print(d.split())
print(d.split(","))
print(d.split("and"))
print(d.count("is"))
print(d.count("and"))
print(d.startswith("my"))
print(d.endswith("MSPA")) 

#LISTS

fruits = ["banana","orange","mango","apples"]
print(fruits[1:3])
fruits.sort()
print(fruits)

num=[1,2,3,4,5]
num.sort()
do = num[::-1]
print(num)
print(do)
c=num[-2:]
print(c)
f=num[-4:-1:-1]
f=num[-1:-4:-1]
print(f)

fruits.remove("banana")
print(fruits)
fruits.append("kiwi")
print(fruits)

new_fruits=[]
new_fruits.append("apple")
print(new_fruits)




