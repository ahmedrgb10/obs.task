
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
        id = int(values[l-1])  
        #print(value[0], evenodd(int(value[2])))
        print('id',id)
