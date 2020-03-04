import sys


def process(cline):
    separated = cline.split(',')
    country = separated[8]
    city = separated[6]
    if not country == 'County':
        print(country, ",", city)


for line in sys.stdin:
    process(line)
