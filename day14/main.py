from pprint import pprint

ans = []

with open("iris.csv") as iris_file:
    header = iris_file.readline().strip().split(',')

    for line in iris_file:
        values = line.strip().split(',')

        new_lst = [values.pop()]
        new_lst = list(map(eval, values)) + new_lst

        tmp = dict(zip(header, new_lst))
        ans.append(tmp)

pprint(ans)
