from typing import Any
from get_data_map import get_data_map
from decorators import iterations_10, iterations_50
from sorts_dict import sorts
import json
import gc
gc.disable()
data_map = generate_data(6, 3, 10)
results = {}
for type in data_map.keys():
    results[str(type)] = {}
    for data_type in data_map[type].keys():
        results[str(type)][data_type] = {}
        for count in data_map[type][data_type].keys():
            results[str(type)][data_type][count] = {}
            for sort in sorts:
                if sort['allowed_types'] != Any and sort['allowed_types'] == type or sort['allowed_types'] == Any:
                    if sort['max_count'] >= count:
                        if count>=50000:
                            results[str(type)][data_type][count][sort["func"].__name__] = iter_10(sort["func"])(data_map[type][data_type][count])
                        else:
                            results[str(type)][data_type][count][sort["func"].__name__] = iter_50(sort["func"])(data_map[type][data_type][count])

with open("results.json", "w") as file:
    json.dump(results, file)
