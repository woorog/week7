import sys
from itertools import *

tc=int(sys.stdin.readline())

for _ in range(tc):
    words=list(str(sys.stdin.readline().strip()))
    a=permutations(words,len(words))
    a=list(set(a))
    for i in a:
        print(''.join(i))