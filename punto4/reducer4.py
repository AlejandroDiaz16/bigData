file = open('prueba4.csv', 'r')
lines = file.readlines()

data = []


def reducer(line):
    # info=line.split(",")
    data.append(int(line))
    data.sort()


for line in lines:
    reducer(line)

for dato in data:
    print(dato)