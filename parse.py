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
    with open('csv_out.csv', 'r', newline='') as inp:
        reader = csv.reader(inp, delimiter=',')
        list_data = list(reader)[1:]
        data = [int(val[1].replace(',', '')) for val in list_data]
    return data


info = get_pure_data()
print(info)
