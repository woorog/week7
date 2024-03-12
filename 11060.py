import sys
from collections import deque

n=int(sys.stdin.readline())
nums=list(map(int,sys.stdin.readline().split()))



q=deque()
vis=set()
count=0
now=0
q.append((count,now))
ans=0
prov=0


while q:
    cnt,number=q.popleft()
    cnt+=1
    if nums[number]==0 or number in vis:
        continue
    vis.add(number)
    if nums[number]+number>=n-1:
        prov=1
        ans=cnt
        break
    for i in range(1,nums[number]+1):
        q.append((cnt,i+number))

if n==1:
    print(0)
elif prov==0:
    print(-1)
else:
    print(ans)
