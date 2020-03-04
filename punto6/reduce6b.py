import sys

data = dict()


def process(cline):
    separated = cline.split(',')
    count = separated[0].strip()
    country = separated[1].strip()
    if count in data:
        data[count] += 1
    else:
        data[count] = 1


for line in sys.stdin:
    process(line)
for k, v in data.items():
    print(v, "\t", k)
