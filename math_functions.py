def get_mean(data):
    return sum(map(lambda i : i[0], data))/len(data)

def get_fashion(data):
    res = 0
    for i in range(1, len(data)):
        if (data[i][1] > data[res][1]): 
            res = i

    return res

def get_mediana(data):
    n = len(data)
    if n % 2 == 0:
        l = n//2 - 1
        r = n//2
        return (data[l][1] + data[r][1])/2
    else:
        return data[n//2][1]

