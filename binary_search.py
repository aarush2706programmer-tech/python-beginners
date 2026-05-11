def binary_search(arr,target):
    low = 0
    high = len(arr)-1
    while low<=high:
        mid = (low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            high = mid-1
        else:
            low = mid+1
    return -1
print(binary_search([1,3,5,8,9,11],9))

def element_sum(arr):
    a = sum(arr)
    return a
print(element_sum([1,2]))

def loop_sum(arr):
    total = 0
    for i in arr:
        total = i+total
    return total
print(loop_sum([1,2]))

def avg(arr):
    total = 0
    for i in arr:
        total = i+total
    avg = total/len(arr)
    return avg
print(avg([1,2,3,4]))

def reverse(arr):
    low = 0
    high = len(arr)-1
    while low<high:
        arr[high],arr[low] = arr[low],arr[high]
        high = high-1
        low = low+1
    return arr        
print(reverse([1,4,5,7,9]))