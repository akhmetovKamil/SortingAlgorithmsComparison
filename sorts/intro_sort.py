from . import heap_sort
import math
def insertion_sort(array, start=0, end=0):
    for i in range(start, end):
        temp_index = i
        while temp_index != start and array[i] < array[temp_index - 1]:
            array[temp_index] = array[temp_index - 1]
            temp_index -= 1
        array[temp_index] = array[i]
    return array
def partition(array, low, high, pivot):
    i = low
    j = high
    while True:
        while array[i] < pivot: i += 1
        j -= 1
        while pivot < array[j]: j -= 1
        if i >= j: return i
        array[i], array[j] = array[j], array[i]
        i += 1
def intro_sort(arr):
    max_depth = 2 * math.log2(len(arr))
    return intro(arr, 0, len(arr) - 1, 5,  int(max_depth))
def intro(array, start, end, size_threshold, max_depth):
    while end - start > size_threshold:
        if max_depth == 0: return heap_sort.heap_sort(array)
        max_depth -= 1
        pivot = sorted(array[start],array[start + (end - start)//2 + 1],array[end - 1])[0]
        p = partition(array, start, end, pivot)
        intro(array, p, end, size_threshold, max_depth)
        end = p
    return insertion_sort(array, start, end)