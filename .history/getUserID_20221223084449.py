
def evenodd(id):
    print('id',id)
    if (id % 2) == 0:
        return 'even'
    else:
        return 'odd'

with open('source.txt') as f:
    for line in f:
        print('\nLINE: ',line)
        values = line.split()

        l = (len(values))

        if values[l-1].isdigit():

            id = int(values[l-1])  
            print(values[l-1], evenodd(int(values[l-1])))
            print('id',id)
