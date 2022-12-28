
def evenodd(id):
    if id/2 == 0:
        return 'even'
    else:
        return 'odd'

with open('source.txt') as f:
   for line in f:
       print(line)
       value = line.split()
       print(value[0], evenodd(value[0]))
       if 'str' in line:
          break