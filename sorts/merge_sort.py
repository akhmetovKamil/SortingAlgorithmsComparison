
def merge_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    center = len(arr) // 2
    return merge_arrays(merge_sort(arr[:center]), merge_sort(arr[center:]))

def merge_arrays(left: list, right: list) -> list:
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

