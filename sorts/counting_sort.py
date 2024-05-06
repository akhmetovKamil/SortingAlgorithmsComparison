
def counting_sort(arr: list) -> list:
    counts_dict = {i: arr.count(i) for i in arr}
    result = []
    for i in sorted(counts_dict):
        result.extend([i]*counts_dict[i])
    return result

