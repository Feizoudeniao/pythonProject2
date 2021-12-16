import csv
import os


def reader(filename):
    # path = '../testdata/' + filename
    # # file = open(path)
    base_path=os.path.dirname(__file__)
    path=base_path.replace('func','testdata/'+filename)
    with open(path) as file:
        table = csv.reader(file)
        list = []
        i = 0
        for row in table:
            if i == 0:
                pass
            else:
                list.append(row)
            i = i + 1

    return list
