arr = ["Apple","Banana","Orange","Grapes"]
print(arr[1])
print(arr[3])

num = [1,3,42,64,5,68,8]
for i in num:
    if i > 10:
        print(i) 


def binary_search(lst,target):
    low = 0
    high = len(lst)-1
    while low<=high:
        mid = (low+high)//2
        if lst[mid]==target:
            return mid
        elif lst[mid]>target:
            high = mid-1
        else:
            low = mid+1
    return -1
print(binary_search([2, 5, 8, 12, 16, 23, 38, 56],23))

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        swap = False
        for j in range(0,n-i-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
                swap = True
        if not swap:
            break
    return lst
print(bubble_sort([2, 5, 8, 12, 16, 23, 38, 56]))  


def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst
print(selection_sort([2, 5, 8, 12, 16, 23, 38, 56]))    


