from math import log, sqrt

def get_mean(data):
    return sum(data)/len(data)

def calc_freq_table(data):
    res = {}
    for x in data:
        if not x in res:
            res[x] = 1
        else:
            res[x] += 1

    return res

def get_fashion(freq_table):
    res_x = None
    res_x_freq = -1
    for x in freq_table:
        if freq_table[x] > res_x_freq:
            res_x = x
            res_x_freq = freq_table[x]

    return res_x

def get_mediana(data):
    n = len(data)
    if n % 2 == 0:
        l = n//2 - 1
        r = n//2
        return (data[l] + data[r])/2
    else:
        return data[n//2]

def get_variance(data):
    mean = get_mean(data)

    return sum(map(lambda x: (x - mean)**2, data))/len(data)

def get_standard_deviation(data):
    return sqrt(get_variance(data))

def get_coeff_of_variation(data):
    return sqrt(get_variance(data))/get_mean(data)

def split_sample(data, n = None):
    def get_n_sets():
        return 1 + int(log(len(data), 2))

    if not n:
        n = get_n_sets()
    #print(f"N intervals = {n}")

    min_value = data[0]
    #print(f"Min value = {min_value}")

    max_value = data[-1]
    #print(f"Max value = {max_value}")
    
    step = (max_value - min_value)/n

    res = [[] for _ in range(n)]

    for i in range(len(data) - 1):
        res[int((data[i] - min_value) / step)].append(data[i])

    res[-1].append(data[-1])

    return res

def get_kvantil(data, alpha):
    n = len(data)
    k = int(alpha*(n - 1))

    if k + 1 < alpha*n:
        return data[min(k + 1, len(data) - 1)]
    elif k + 1 == alpha*n:
        return (data[min(k + 1, len(data) - 1)] + data[k])/2
    else:
        return data[k]

def remove_outliers(data):
    x25 = get_kvantil(data, 0.25)
    x75 = get_kvantil(data, 0.75)

    print(f"X25 = {x25}")
    print(f"X75 = {x75}")
    interval = (x25 - 1.5*(x75 - x25), x75 + 1.5*(x75 - x25))
    print(interval)

    return list(filter(lambda e: interval[0] <= e <= interval[1], data))

