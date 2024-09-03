from parse import get_pure_data
from math_functions import *

data = get_pure_data()
print(data)

freq_table = calc_freq_table(data)

print(freq_table)

fashion = get_fashion(freq_table)
print(fashion)

splits = split_sample(data)
print(splits)

