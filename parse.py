import csv

rows = []

# with open("c:\\users\\user\\desktop\\data.txt", "r") as f:
#     for line in f:
#         l = line[:-1].split('\t')
#         rows.append({'year': l[0], 'deaths': l[1]})
#
#
# with open('csv_out.csv', 'w', newline='') as csv_out:
#     wr = csv.DictWriter(csv_out, quoting=csv.QUOTE_ALL, fieldnames=['year', 'deaths'])
#     wr.writeheader()
#     wr.writerows(rows)


def get_pure_data() -> list[int]:
    #with open('csv_out.csv', 'r', newline='') as inp:
    #    reader = csv.reader(inp, delimiter=',')
    #    list_data = list(reader)[1:]
    #    data = [int(val[1].replace(',', '')) for val in list_data]
    #return sorted(data)

    # from 2016 to 2021
    return [
        55, 49, 34, 54, 55, 55, 135, 47, 36, 134, 56, 46,
        37, 25, 60, 72, 28, 53, 150, 83, 80, 78, 45, 69,
        37, 29, 46, 30, 53, 47, 169, 59, 44, 46, 31, 55,
        47, 16, 40, 4, 67, 55, 120, 91, 49, 31, 68, 68,
        38, 49, 22, 11, 52, 134, 68, 62, 31, 47, 51, 49,
        109, 39, 34, 43, 113, 84, 41, 74, 119, 10, 60, 55,
    ]

