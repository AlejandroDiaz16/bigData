import sys


def process(cline):
    separated = cline.split(',')
    year = separated[2].split('-')[0]
    month = separated[2].split('-')[1]
    if year.isdigit():
        print(year, ",", month)


for line in sys.stdin:
    process(line)