from typing import List
def lsd_radix_sort(arr: List[int]) -> List[int]:
    placement = 1
    while placement <= max(arr):
        buckets = [[] for _ in range(13)]
        for i in arr:
            tmp = int((i / placement) % 13)
            buckets[tmp].append(i)
        a = 0
        for b in range(13):
            for i in buckets[b]:
                arr[a] = i
                a += 1
        placement *= 13
    return arr
