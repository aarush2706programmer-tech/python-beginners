a = "Aarush"
print(a[0:5:1])
print(a[0:6])
print(a[3:5:1])

x = 5
y=15
for i in range(1,11):
    print(x,"x",i,"=",x*i)

for i in range(1,11):
    print(y,"x",i,"=",y*i)

a = input("Enter your name: ")
b=input("Enter your age: ")
c = input("Enter your city: ")
d = input("Enter your mobile number: ")
print(f"Your name is {a}, your age is {b}, you live in {c} and your mobile number is {d}.")