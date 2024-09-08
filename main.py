from math import ceil, exp, floor
from parse import get_pure_data
from math_functions import *
from support import separate

def print_data_set(data):
    for n in data:
        print(n)

class SplitInfo:
    def __init__(self, split, mean, variance, standard_deviation) -> None:
        self.mean = mean
        self.variance = variance
        self.standard_deviation = standard_deviation
        self.split = split

class VariancesInfo:
    def __init__(self, general_variance, in_variance, between_variance) -> None:
        self.general_variance = general_variance
        self.in_variance = in_variance
        self.between_variance = between_variance

def get_split_infos(splits):
    split_infos = []

    for i in range(len(splits)):
        curr_split = splits[i]
        #print(f"Split No {i}:  {curr_split}")
        
        curr_mean = get_mean(curr_split)
        #print(f"Mean = {curr_mean}")

        curr_variance = get_variance(curr_split)
        #print(f"Variance = {curr_variance}")

        standard_deviation = get_standard_deviation(curr_split)
        #print(f"Standard deviation: {standard_deviation}")
        
        split_infos.append(SplitInfo(curr_split, curr_mean, curr_variance, standard_deviation))

    return split_infos

def print_split_infos(split_infos):
    print(f"N intervals = {len(split_infos)}")
    print()

    for i in range(len(split_infos)):
        print(f"Split No {i + 1} (len = {len(split_infos[i].split)}):")
        print_data_set(split_infos[i].split)
        print()

def calc_variances_info(split_infos, general_mean, data):
    def calc_general_variance(split_infos):
        return get_variance(data)

    def calc_in_group_variance(split_infos):
        return sum((len(split_info.split)*split_info.variance for split_info in split_infos))/len(data)

    def calc_between_group_variance(split_infos):
        temp_variances = [((curr_split.mean - general_mean)**2)*len(curr_split.split) for curr_split in split_infos]
        between_group_variance = sum(temp_variances)/len(data)
        return between_group_variance

    return VariancesInfo(
        calc_general_variance(split_infos),
        calc_in_group_variance(split_infos),
        calc_between_group_variance(split_infos),
    )

def get_determination_coeff(variances_info):
    return variances_info.between_variance / variances_info.general_variance

data = get_pure_data()
data.sort()

print("1. Source data:")
print_data_set(data)

separate()

freq_table = calc_freq_table(data)

print("2.1 ")
fashion = get_fashion(freq_table)
print(f"Fashion = {fashion}")

mediana = get_mediana(data)
print(f"Mediana = {mediana}")

mean = get_mean(data)
print(f"Mean = {mean}")

variance = get_variance(data)
print(f"Variance = {variance}")

variation_coeff = get_coeff_of_variation(data)
print(f"Variation coeff = {variation_coeff}")

separate()

print("2.2") #https://wiki.loginom.ru/articles/variation-coefficient.html
if variation_coeff < 0.10:
    print("<10%")
elif variation_coeff < 0.20:
    print("<20%")
elif variation_coeff < 0.33:
    print("<33%")
else:
    print("too big")

separate()
#print(freq_table)

print("2.3")

separate()

print("2.4")

splits = split_sample(data)

split_infos = get_split_infos(splits)
print_split_infos(split_infos)

separate()

print("2.5")

separate()

print("2.6")
print("I supposed that value of the first interval = 0, second = 1 and so on...")

mean = sum([len(split_infos[i].split) for i in range(len(split_infos))])/len(data)
print(f"Mean = {mean}")
print(f"Variance = {variance}")
print(f"Standard quadratic ... = {sqrt(variance)}")

separate()

print("2.7")

variances_info = calc_variances_info(split_infos, get_mean(data), data)

print("General:")
print(variances_info.general_variance)
print("In")
print(variances_info.in_variance)
print("Between")
print(variances_info.between_variance)

print("General - (In + Between):")
print(variances_info.general_variance - (variances_info.in_variance + variances_info.between_variance))

print(f"Determination coeff = {get_determination_coeff(variances_info)}")

separate()

print("2.8")

def get_n_sets():
    return 1 + int(log(len(data), 2))

def task_2_8(data, n_intervals):
    splits = split_sample(data, n_intervals)

    split_infos = get_split_infos(splits)

    variances_info = calc_variances_info(split_infos, get_mean(data), data)

    print(f"Determination coeff = {get_determination_coeff(variances_info)}")

print("For n_intervals - 1:")

task_2_8(data, n_intervals=get_n_sets() - 1)

print("For n_intervals + 1:")

task_2_8(data, n_intervals=get_n_sets() + 1)

separate()

print("2.9")

print("Предполагаемое распределение - распределение Пуассона")

def get_intervals(data, n_intervals):
    intervals = []

    min_value = data[0]
    max_value = data[-1]

    delta = max_value - min_value
    for i in range(n_intervals):
        intervals.append((min_value + i*delta, min_value + (i + 1)*delta))

    return intervals

def factorial(n):
    res = 1
    for i in range(2, n + 1):
        res *= i

    return res
    
def calc_poisson(x: int, mean):
    return (int(mean)**x/factorial(x))*exp(-mean)

def calc_poisson_interval_prob(mean, l, r):
    l = ceil(l)
    r = floor(r)

    res = 0
    for i in range(l, r + 1):
        res += calc_poisson(i, mean)

    return res

def chi_square_check(split_infos, data):
    n = len(data)

    mean = get_mean(data)
    print(mean)

    n_intervals = len(split_infos)

    intervals = get_intervals(data, n_intervals)

    p = [calc_poisson_interval_prob(mean, intervals[i][0], intervals[i][1]) for i in range(len(intervals))]
    print(p)

    res = [((len(split_infos[i].split) - n*p[i])**2)/(n*p[i]) for i in range(len(split_infos))]
    print(res)

    return sum(res)

print(f"Chi square = {chi_square_check(split_infos, data)}")

#split_infos = []
#
#for i in range(len(splits)):
#    curr_split = splits[i]
#    print(f"Split No {i}: {curr_split}")
#    
#    curr_mean = get_mean(curr_split)
#    print(f"Mean = {curr_mean}")
#
#    curr_variance = get_variance(curr_split)
#    print(f"Variance = {curr_variance}")
#
#    standard_deviation = get_standard_deviation(curr_split)
#    print(f"Standard deviation: {standard_deviation}")
#    
#    split_infos.append(SplitInfo(curr_split, curr_mean, curr_variance, standard_deviation))
#
#in_group_variance = sum((len(split_info.split)*split_info.variance for split_info in split_infos))/len(data)
#print(f"In group variance = {in_group_variance}")
#
#temp_variances = [((curr_split.mean - mean)**2)*len(curr_split.split) for curr_split in split_infos]
#between_group_variance = sum(temp_variances)/len(data)
#print(f"Between group variance = {between_group_variance}")
#
#print(f"Between group variance / variance: {between_group_variance / variance}")

