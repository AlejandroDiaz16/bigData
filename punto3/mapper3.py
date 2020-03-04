import sys

def process(line):
    info = line.split(",")
    city = info[6]
    price = info[1]
    print(city+"/"+price)

for line in sys.stdin:
    process(line)
