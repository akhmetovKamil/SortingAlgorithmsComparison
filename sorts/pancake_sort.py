
def pancake_sort(arr: list) -> list:
    for cur in range(len(arr), 1, -1):
        temp = arr.index(max(arr[:cur]))
        arr = arr[temp::-1] + arr[temp + 1:] if temp else arr[::-1]
    return arr