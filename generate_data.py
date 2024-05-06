from typing import List, Tuple
from generators import *


def generate_data(cf: int, f: int, l: int):
    gens = [
        {"function":generate_bytes_arr,"type":bytes,},
        {"function":generate_strings_arr,"type":str,},
        {"function":generate_integers_arr,"type":int,},
        {"function":generate_structs_arr,"type":Student,}]
    results = {}
    for val in gens:
        gen_func = val["function"]
        gen_type = val["type"]
        results[gen_type] = {'random_generation': {}, 'tail_random_generation': {}, 'insert_random_generation': {}, 'often_random_generation': {}}
        for i in range(1,cf):
            length = (10**i)*5
            coef = int(length/10)
            results[gen_type]['random_generation'][length] = gen_func(length, f, l)
            results[gen_type]['tail_random_generation'][length] = generate_partially_random(gen_type, length, f, l, coef, "tail")
            results[gen_type]['insert_random_generation'][length] = generate_partially_random(gen_type, length, f, l, coef, "insert")
            results[gen_type]['often_random_generation'][length] = generate_repeated_value(gen_type, length, f)
    return results


