import random as r
import time as t
import sorting as s
import pprint as p
from matplotlib import pyplot as plt
import json

amount_numbers_min = 1_000
amount_numbers_max = 10_000
amount_step = 500
max_vol = 100_000
__LIST_OF_SORT = {s.MergeSort, s.QuickSort}
#__LIST_OF_SORT = {s.SelectionSort, s.InsertionSort, s.MergeSort, s.QuickSort}
#__LIST_OF_SORT = {s.SelectionSort, s.InsertionSort, s.MergeSort, s.QuickSort, s.RadixSort, s.BubbleSort, s.BubbleSortWithBrake}

__DICT_OF_RESULT = {}

for iteration in range(amount_numbers_min, amount_numbers_max + 1, amount_step):
    _data = []
    _data.clear()
    _data = [r.randint(1, max_vol) for _ in range(iteration)]

    for type_of_alg in __LIST_OF_SORT:
        alg = type_of_alg(_data.copy())

        # print(alg.data)
        time_begin = t.time()

        alg.start_sorting(alg.data)

        time_sort = t.time() - time_begin
        # print(alg.data)

        if not __DICT_OF_RESULT.get(type_of_alg.__name__, False):
            __DICT_OF_RESULT[type_of_alg.__name__] = [(iteration, time_sort)]
        else:
            __DICT_OF_RESULT[type_of_alg.__name__].append((iteration, time_sort))

        print(f"{type_of_alg.__name__}:{time_sort}")

p.pprint(__DICT_OF_RESULT)

#Save in JSON file
with open("create_data_file.json", "w") as write_file:
    json.dump(__DICT_OF_RESULT, write_file)

#Load from JSON file
with open("create_data_file.json", "r") as read_file:
    __DICT_OF_RESULT = json.load(read_file)

#Show plot
plt.xkcd()
for type_of_alg in __LIST_OF_SORT:
    ages_y = [type_alg[1] for type_alg in __DICT_OF_RESULT.get(type_of_alg.__name__)]
    ages_x = [type_alg[0] for type_alg in __DICT_OF_RESULT.get(type_of_alg.__name__)]

    plt.plot(ages_x, ages_y, label=type_of_alg.__name__)

plt.xlabel('Amount of numbers')
plt.ylabel('Time, sec')
plt.title('Algorithms of sorting')

plt.legend()
plt.tight_layout()
plt.savefig('plot.png')

plt.show()