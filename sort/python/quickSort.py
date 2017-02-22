import random

def quickSort(arr):
    return sort(0, len(arr)-1)

def sort(left, right):
    if left == right:
        return

    i, j = left, right
    pivotIndex = random.randint(left, right)

    pivot = arr[pivotIndex]

    while i < j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i <= j:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1
            j -= 1
    if left < j:
        sort(left, j)
    if right > i:
        sort(i, right)
    return arr

def fillArray():
    arr = []
    for i in xrange(6):
        arr.append(random.randrange(20))
    return arr

arr = fillArray()
arr = quickSort(arr)
print arr



