import sys

data = dict()
count = dict()


def process(cline):
    separated = cline.split(',')
    country = separated[0].strip()
    city = separated[1].strip()
    if country in data:
        if city not in count:
            data[country] += 1
            count[city] = 1
    else:
        data[country] = 1


for line in sys.stdin:
    process(line)
for k, v in data.items():
    print(k, ",", v)
