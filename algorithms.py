def bubbleSort(array: list) -> None:
    n = len(array)
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                swapped = True
                array[j], array[j + 1] = array[j + 1], array[j]
        if not swapped:
            return

def insertionSort(array: list) -> None:
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key


def partition(array: list, low: int, high: int) -> int:
    i = (low - 1)
    pivot = array[high]
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return (i + 1)

def quickSort(array: list, low: int, high: int) -> None:
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)


arr = [123, 1, 22, 22, -3, 4, -5]
bubbleSort(arr)
print(arr)

arr = [123, 1, 22, 22, -3, 4, -5]
insertionSort(arr)
print(arr)

arr = [123, 1, 22, 22, -3, 4, -5]
quickSort(arr, 0, len(arr) - 1)
print(arr)

