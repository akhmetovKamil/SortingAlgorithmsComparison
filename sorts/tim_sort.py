
def merge_sort(arr, start, mid, end):
    if mid == end:
        return arr
    first, last = arr[start:mid+1], arr[mid+1:end+1]
    ind1 = ind2 = 0
    for ind in range(start, end+1):
        if ind1 < len(first) and (ind2 == len(last) or first[ind1] < last[ind2]):
            arr[ind] = first[ind1]
            ind1 += 1
        else:
            arr[ind] = last[ind2]
            ind2 += 1
    return arr
def tim_sort(arr: list) -> list:
    n = len(arr)
    for start in range(0, n, 30):
        end = min(start+30-1, n-1)
        arr = insertion_sort(arr, start, end)
    curr_size = 30
    while curr_size < n:
        for start in range(0, n, curr_size*2):
            mid = min(n-1, start+curr_size-1)
            end = min(n-1, mid+curr_size)
            arr = merge_sort(arr, start, mid, end)
        curr_size *= 2
    return arr
