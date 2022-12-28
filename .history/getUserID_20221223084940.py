
def evenodd(id):
    if (id % 2) == 0:
        return 'even'
    else:
        return 'odd'

with open('source.txt') as f:
    for line in f:
        print('\nLINE: ',line)

        # split values
        values = line.split()
        l = (len(values))

        #check if value is digit - determine EvenOdd
        if values[l-1].isdigit():
            id = int(values[l-1])  
            print(id, evenodd(id))
        else

        
        

