def get_mean(data):
    return sum(map(lambda i : i[0], data))/len(data)

def get_fashion(data):
    res = 0
    for i in range(1, len(data)):
        if (data[i][1] > data[res][1]): 
            res = i

    return res

