import sys

N,suchi,eat,bonus=map(int,sys.stdin.readline().split())
cnt=0
belt=[]
check=[0]*3000001
for _ in range(N):
    belt.append(int(sys.stdin.readline()))

belt=belt+belt
test=belt[:eat]
for i in test:
    check[i]+=1

SP=0
EP=eat
test=set(test)
ans=len(test)
for i in range(eat,N+eat+1):
    check[belt[i]]+=1
    check[belt[SP]]-=1
    test.add(belt[i])
    if check[belt[SP]]==0:
        test.remove(belt[SP])
    SP+=1
    if bonus in test:
        k=len(test)
    else:
        k=len(test)+1
    if k>ans:
        ans=k

print(ans)