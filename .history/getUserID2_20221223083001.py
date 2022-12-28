
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
        print(len(values))
        if values[2] is not None:
            id = int(values[2])  
        #print(value[0], evenodd(int(value[2])))
        print('id',id)
