def multiply(a,b=2):
    return a*b

def describe(n):
    double = multiply(n)
    triple = multiply(n,3)
    return double,triple

d,t = describe(5)
print(d)
print(t)
print(multiply(d,t))

def celsius_fahrenheit(c):
    return (c*9/5)+32

def classify(c):
    temp = celsius_fahrenheit(c)
    if c>35:
        print("Hot")
    elif c >=20:
        print("Warm")
    
    else:
        print("Cold")

a = classify(38)
b = classify(25)
c = classify(10)

a = ["Apple","Banana","Cherry","Mango"]
def find_longest_word(a):
    longest =  a[0]
    for b in a:
        if len(b)>len(longest):
            longest=b
    return longest
c = find_longest_word(a)
print(c)

for i in range(1,6):
    print("*"*i)
    
count = 0

while True:
    num = int(input("Enter a number"))
    print("Enter again")
    if num<=0:
        print("You entered 0 or below")
        break
    count = count+num
print(count)
    


        

