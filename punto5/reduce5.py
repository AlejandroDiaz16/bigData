import sys

KEY_CONST = "{0}-{1}"

data = dict()
maxi = dict()


def process(cline):
    separated = cline.split(',')
    year = separated[0].strip()
    month = separated[1].strip()
    key = KEY_CONST.format(year, month)
    if key in data:
        data[key] += 1
    else:
        data[key] = 1


for line in sys.stdin:
    process(line)

for k in data.keys():
    values = k.split('-')
    if values[0] in maxi:
        maxi_key = KEY_CONST.format(values[0], maxi[values[0]])
        if data[k] > data[maxi_key]:
            maxi[values[0]] = values[1]
    else:
        maxi[values[0]] = values[1]

for k, v in maxi.items():
    print(k, v)
