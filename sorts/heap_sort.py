
def heap(arr: list, i: int, size: int) -> None:
    max_value = i
    l = 2 * i + 1
    r = l + 1
    max_value = l if l < size and arr[l] > arr[max_value] else max_value
    max_value = r if r < size and arr[r] > arr[max_value] else max_value
    if max_value != i:
        arr[max_value], arr[i] = arr[i], arr[max_value]
        heap(arr, max_value, size)
def heap_sort(arr: list) -> list:
    for i in range(len(arr) // 2 - 1, -1, -1):
        heap(arr, i, len(arr))
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heap(arr, 0, i)
    return arr

