file = open('prueba1.csv', 'r')
lines = file.readlines()


def process(line):
    info = line.split(",")
    year = info[2].split("-")[0]
    name = info[6]
    if year == 2015 and name == "STAMFORD":
        print(info[1])


for line in lines:
    process(line)
