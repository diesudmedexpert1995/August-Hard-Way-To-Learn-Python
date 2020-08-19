def binary_search(arr, item):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low+high) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

mylist = [1,2,5,7,9,10,24,67]

print(binary_search(mylist, 4))
print(binary_search(mylist, 10))
print(binary_search(mylist, -1))
