
def quick_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    pivot = sorted(arr[0], arr[len(arr)//2], arr[-1])[1]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return quick_sort(less) + equal + quick_sort(greater)