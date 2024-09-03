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

def get_coeff_of_variation(data):
    return get_variance(data)/get_mean(data)

