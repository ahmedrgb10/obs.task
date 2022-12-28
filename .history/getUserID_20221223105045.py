
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

def fqdn(hostname):
    if hostname.endswith('.'):
        hostname = hostname[:-1]
    if len(hostname) < 1 or len(hostname) > 253:
        return False
    
    pattern = re.compile('^[a-z0-9]([@[a-z0-9-]{0,61}[a-z0-9])?$',re.IGNORECASE)
    labels = hostname.split('.')
    for label in labels:
        matched = pattern.match(label)

        if matched:
            flag='routable'
        else:
            flag='Not routable'
            return flag      
    return flag    


with open('source.txt') as f:
    for line in f:
        print('\nLINE: ',line)
        # split values
        values = line.split()
        l = (len(values))
        mail = values[1]
        #check if value is digit - determine EvenOdd
        if values[l-1].isdigit():
            id = int(values[l-1])  
            print('the ID ' id + 'of the user ' + mail + ' is ' , evenodd(id))      
        
        
        #isfqdn = is_fqdn(mail)
        isfqdn = fqdn(mail)
        print(mail,isfqdn)