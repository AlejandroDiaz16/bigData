file = open('prueba3.csv', 'r')
lines = file.readlines()

data = dict()


def reducer(line):
    city = line.split("/")
    # print(city[1])
    if city[0] in data:
        if data[city[0]] > city[1]:
            data[city[0]] = city[1]
    else:
        data[city[0]] = city[1]


for line in lines:
    reducer(line)

for datos in data:
    print(datos + " " + data[datos])
