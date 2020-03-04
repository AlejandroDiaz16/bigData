import sys


def process(cline):
    separated = cline.split(',')
    year = separated[2].split('-')[0]
    if year.isdigit():
        print(year)


for line in sys.stdin:
    process(line)
