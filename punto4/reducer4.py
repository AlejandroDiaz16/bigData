import sys

data = []


def reducer(line):
    # info=line.split(",")
    data.append(int(line))
    data.sort()


for line in sys.stdin:
    reducer(line)

for dato in data:
    print(dato)
