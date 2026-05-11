a = [10,45,67,23,31]
min_value = a[0]
for num in a:
    if min_value>num:
        min_value=num
print("The minimum number is : ",min_value)

b = [5,8,2,10,7]
x = 11
found = False
for element in b:
    if element == x:
        found = True
print(found)