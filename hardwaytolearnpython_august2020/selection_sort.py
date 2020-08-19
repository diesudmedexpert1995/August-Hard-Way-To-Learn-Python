def find_smallest(arr):
    smallest = arr[0] # в качестве  найменьшего элемента возьмем первый элемент
    smallest_index = 0 # индекс найменьшего елемента в исходном состоянии
    for i in range(1, len(arr)):
        # если текущий елемент менше найменьшего
        if arr[i] < smallest:
            # указываем его в качестве найменьшего
            smallest = arr[i]
            # указываем его индекс
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


print(selectionSort([2,7,6,1,5,0,8]))
