import sys

n,T=map(int,sys.stdin.readline().split())

nums=list(map(int,sys.stdin.readline().split()))

p,ep=0,1
ans=99999999999999
sumlist=[nums[0]]
for i in range(1,n):
    sumlist.append(sumlist[i-1]+nums[i])



if sumlist[p]>=T:
    ans=1


def Tpointer(sumlist, p, ep):
    for i in range(p,ep):
        if sumlist[ep]-sumlist[i]<T:
            break
        else:
            p=i
    return p



for i in range(n):
    ep=i
    if sumlist[ep]-sumlist[p]>=T:
        newp=Tpointer(sumlist,p,ep)
        p=newp
        if ep-p<ans:
            ans=ep-p




if ans==99999999999999:
    print(0)
else:
    print(ans)