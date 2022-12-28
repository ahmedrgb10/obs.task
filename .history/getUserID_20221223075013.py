file = open("source.txt", "r")

for line in file:
    values = line.split()
    print(values)
    print('In', values[0], 'the average temp. was', values[1], '°C and CO2 emmisions were', values[2], 'gigatons.')

file.close()