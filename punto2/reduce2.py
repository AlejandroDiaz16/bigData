import sys

data = dict()
count = dict()


def process(cline):
    separated = cline.split(',')
    city = separated[0]
    price = separated[1]
    if city in data:
        count[city] += 1
        data[city] += int(price.strip())
    else:
        count[city] = 1
        data[city] = int(price.strip())


for line in sys.stdin:
    process(line)
for k, v in data.items():
    print(k, ",", int(v) / int(count[k]))
