def linear_search(lst,target):
    for i,x in enumerate(lst):
        if x == target:
            return i
    return -1
print(linear_search([10,20,30,40],30))

a = ["Avengers","Harry Potter","Sonic","Conjuring","Batman"]
for element in a:
    if element == "Avengers":
        print("Founded")
        break
    else:
       print("Not founded")

def count_target(lst,target):
    x = 0
    for i in lst:
        if i == target:
            x = x+1
    print(x)
count_target([10,20,40,59,89,40,32,40],40)

def find_all_positions(lst,target):
    for i,x in enumerate(lst):
        if x == target:
            print(i,end = " ")
find_all_positions([10,20,40,59,89,40,32,40],40)

def find_max(lst):
    min_value = lst[0]
    for num in lst:
        if min_value > num:
            min_value=num
    print(min_value)
find_max([10,20,121,1,89,7,32,201])
