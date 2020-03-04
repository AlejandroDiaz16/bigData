import sys


def process(cline):
    separated = cline.split(',')
    price = separated[1]
    city = separated[6]
    if price.isdigit():
        print(city, ",", price)


for line in sys.stdin:
    process(line)
