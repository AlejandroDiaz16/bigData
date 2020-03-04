import sys


def process(cline):
    separated = cline.split(',')
    country = separated[0]
    count = int(separated[1].strip())
    print(count, ",", country)


for line in sys.stdin:
    process(line)
