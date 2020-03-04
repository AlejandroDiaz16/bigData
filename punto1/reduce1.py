import sys

data = dict()


def process(year):
    year = year.strip()
    if year in data:
        data[year] += 1
    else:
        data[year] = 1


for line in sys.stdin:
    process(line)
for info in data:
    print(info, ',', data[info])
