import sys


def process(line):
    info = line.split(",")
    year = info[2].split("-")[0]
    name = info[6]
    if year == 2015 and name == "STAMFORD":
        print(info[1])


for line in sys.stdin:
    process(line)
