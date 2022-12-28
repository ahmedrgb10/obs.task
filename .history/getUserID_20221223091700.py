
import re

def evenodd(id):
    if (id % 2) == 0:
        return 'even'
    else:
        return 'odd'

def is_fqdn(address):
    def is_fqdn(hostname):
        return re.match(r'^(?!.{255}|.{253}[^.])([a-z0-9](?:[-a-z-0-9]{0,61}[a-z0-9])?\.)*[a-z0-9](?:[-a-z0-9]{0,61}[a-z0-9])?[.]?$', hostname, re.IGNORECASE)


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
        
        else:
            mail = values[l-1]
        
        mail = values[l-1]