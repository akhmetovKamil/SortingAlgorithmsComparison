
def selection_sort(arr: list) -> list:
    for i in range(len(arr)):
        index = i
        for j in range(i+1, len(arr)):
            index = j if arr[j] < arr[index] else index
        arr[i], arr[index] = arr[index], arr[i]
    return arr
