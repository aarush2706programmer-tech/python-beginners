def greet(name,age=12):
    print(name,age)

greet("Aarush",15)
greet(15,"Aarush")


def add(a,b):
    return a + b
 
add(20,30)
result = add(20,30)
print(result)

numbers = [1,2,3,4,5]
def min_max(nums):
    print(min(nums))
    print(max(nums))

min_max(numbers)

a = 7
def square(x):
    return x**2
print(square(a))

def square():
    b=7
    return b**2
print(square())
#print(b) will give an error because b is a local variable and cannot be accessed outside the function.

def analyse_word(word):
    return len(word), word.upper(), word[::-1]
 
lenght,upper,reverse = analyse_word("Aarush")
print(lenght)
print(upper)
print(reverse)

x=100
def double(v):
    result = v*2
    return result
double(5)
result = double(5)
print(result)

print(double(x))

def sum_of_squares(a,b):
    print(a**2 + b**2)

sum_of_squares(3,4)

def calculate_price(price, discount = 10):
    saving = price * (discount / 100)
    return price - saving

print(calculate_price(500)) 