"""def sum(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum+i
    print(sum)
sum(20)

a = input("Enter something")
b = input("Enter something")
c = input("Enter something")
print(str(a)*int(a) + str(b)*int(b) + c)

#Swapping two variables
d = 20
e = 10
d,e=e,d
print(d,e)
 
f = "Aarush"
print(d is e)

g = [1,2,3]
print(1 in g)

h = ["Aarush","Advik","Vihaan"]
for i,name in enumerate(h,start = 10):
    print(i,name)"""

for i in range(1,4):
    for j in range(1,4):
        #print(i,j)
        print(i*j , end =" ")
    print()

for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

rows = 5
for i in range(rows):
    for j in range(rows):
        print("*",end = " ")
    print()

for i in range(1,rows+1):
    for j in range(i):
        print("*",end = " ")
    print()

for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()

for i in range(rows,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

for i in range(1,11):
    for j in range(1,11):
        print(i*j,end = " ")
    print()

for i in range(1,6):
    for j in range(1,4):
        print("*",end = " ")
    print()

first = [2,4,6]
second = [2,4,6]
for i in first:
    for j in second:
        if i==j:
            continue
        print(i,"x",j,"=",i*j)

final = []
for i in first:
    for j in second:
        final.append(i+j)
    print(final)

i = 1
while i <=5:
    j = 1
    while j <=10:
        print(j,end=" ")
        j = j+1
    i = i+1
    print()

print("Perfect numbers from 1 to 100")
n = 2
while n<=100:
    x_sum = 0
    for i in range(1,n):
        if n%i==0:
            x_sum +=i
    if x_sum ==n:
        print("Perfect number : ",n)
    n +=1

