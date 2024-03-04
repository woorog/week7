import sys

n=int(sys.stdin.readline())

lists=[0]*(n+1)
lists[0]=1
lists[1]=2
lists[2]=7

dplist=[0]*(n+1)
for i in range(3,n+1):
    dplist[i]+=lists[i-3]
    lists[i]=(lists[i-1]*3+dplist[i])%1000000007
print(lists[n])