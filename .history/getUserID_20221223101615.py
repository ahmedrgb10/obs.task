
import re

def evenodd(id):
    if (id % 2) == 0:
        return 'even'
    else:
        return 'odd'


def is_fqdn(hostname):
    if hostname[-1] == ".":
        # strip exactly one dot from the right, if present
        hostname = hostname[:-1]
    
    if len(hostname) > 253:
        return False

    labels = hostname.split(".")
    print(labels)
    # the TLD must be not all-numeric
    if re.match(r"[0-9]+$", labels[-1]):
        return False

    allowed = re.compile(r"(?!-)[a-z0-9-]{1,63}(?<!-)$", re.IGNORECASE)
    print('allowed', allowed)
    return all(allowed.match(label) for label in labels)

def fqdn(dn):
    if dn.endswith('.'):
        dn = dn[:-1]
    if len(dn) < 1 or len(dn) > 253:
        return False
    ldh_re = re.compile('^[a-z0-9]([a-z0-9-]{0,61}[a-z0-9])?$',re.IGNORECASE)
    #print('ldh',ldh_re)
    #return all(ldh_re.match(x) for x in dn.split('.'))

    labels = dn.split('.')
    for label in labels:
        print('label',label,ldh_re.match(label))

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
        
        mail = values[1]
        #isfqdn = is_fqdn(mail)
        isfqdn = fqdn(mail)
        print(mail,isfqdn)