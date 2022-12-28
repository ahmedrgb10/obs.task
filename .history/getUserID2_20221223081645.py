
def evenodd(id):
    print('id',id)
    if (id % 2) == 0:
        return 'even'
    else:
        return 'odd'

with open('source.txt') as f:
    for line in f:
       print(line)
       value = line.split()

       print(value[0], evenodd(int(value[2])))
       if 'str' in line:
          break
