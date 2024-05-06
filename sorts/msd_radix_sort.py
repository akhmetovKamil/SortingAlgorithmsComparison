from typing import List
def msd_radix_sort(arr: List[int]) -> List[int]:
    exp = 1
    while max(arr)//exp > 0:
        exp *= 10
    exp //= 10
    return _msd_radix_sort(arr, exp)
def _msd_radix_sort(arr: List[int], exp: int) -> List[int]:
    if exp < 1:
        return arr
    output = [0] * len(arr)
    count = [0] * 10
    for num in arr:
        index = num // exp
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = len(arr) - 1
    while i >= 0:
        num = arr[i]
        index = num // exp
        output[count[index % 10] - 1] = num
        count[index % 10] -= 1
        i -= 1
    i = 0
    for i in range(len(arr)):
        arr[i] = output[i]
    next_exp = exp // 10
    for i in range(10):
        start = count[i]
        end = count[i + 1] if i + 1 < 10 else len(arr)
        _msd_radix_sort(arr[start:end], next_exp)
    return arr