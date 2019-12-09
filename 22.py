import sys
import re
s=[]
c=input()
v=re.findall('[()[\\]{}]',c)

def cocie(left, right):
    return left+right in['()','[]','{}']

for b in v:
    if b in '([{':
        s.append(b)
    else:
        if len(s)==0:
            print('no')
            sys.exit(0)
        if not cocie(s.pop(), b):
            print('no')
            sys.exit(0)

if len(s) == 0:
    print('Yes')
else:
    print('no')
