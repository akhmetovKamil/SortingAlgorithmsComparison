import random
from typing import Callable, List
from structure import Student
import string
def generate_integers_arr(count: int, f: int, l: int) -> List[int]:
    return [random.randint(f, l) for _ in range(count)]
def generate_bytes_arr(count: int, f: int = 0, l: int = 9) -> List[bytes]:
    return [(random.randint(f, l)).to_bytes() for _ in range(count)]
def generate_strings_arr(count: int, f: int = 5, l: int = 10, weight: int = 1) -> List[str]:
    return [''.join(random.choices(string.ascii_letters, weights=[weight, weight]+[1 for _ in range(50)], k=random.randint(f, l))) for _ in range(count)]
def generate_structs_arr(count: int, f: int, l: int) -> List[Student]:
    return [Student(average_score=random.randint(f, l), name=''.join(random.choices(string.ascii_letters)))]
def generate_repeated_value(gen_type: type, count: int, f: int) -> list:
    if gen_type == str:
        return generate_strings_arr(count, 2, 2, 1000)
    elif gen_type == int:
        return generate_integers_arr(count, f, f+1)
    elif gen_type == bytes:
        return generate_bytes_arr(count, f, f+1)
    elif gen_type == Student:
        return generate_structs_arr(count, f, f+1)
def generate_partially_random(type: type, count: int, f: int, l: int, random_elements_count: int, gen_type: str) -> list:
    generate_func: Callable[[int, int, int], List[type]]
    arr: List[type] = []
    if type == str:
        alph = string.ascii_letters
        max_count = (count-random_elements_count) // len(alph)
        break_flag = False
        for el in alph:
            if break_flag:
                break
            for i in range(f, f+max_count+1):
                if len(arr) == (count-random_elements_count):
                    break_flag = True
                    break
                arr.append(el*i)
        generate_func = generate_strings_arr
    elif type == int:
        generate_func = generate_integers_arr
        arr = [i for i in range(1, count-random_elements_count)]
    elif type == bytes:
        l = 255 if l > 256 else l+1
        max_count = (count-random_elements_count) // l
        break_flag = False
        for i in range(l):
            if break_flag:
                break
            for _ in range(max_count):
                if len(arr) == (count-random_elements_count):
                    break_flag = True
                    break
                arr.append(i.to_bytes())
        generate_func = generate_bytes_arr
    elif type == Student:
        generate_func = generate_structs_arr
        arr = [Student(average_score=i, name=''.join(random.choices(string.ascii_letters)))
               for i in range(1, count-random_elements_count)]
    random_arr: List[type] = generate_func(random_elements_count, f, l)
    if gen_type == "tail":
        arr += random_arr
    elif gen_type == "insert":
        for el in random_arr:
            arr.insert(random.randint(0, len(arr)-1), el)
    return arr
