with open('source.txt') as f:
   for line in f:
       print(line)
       #value = line.split()
       #print(value)
       if 'str' in line:
          break