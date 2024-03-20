import heapq
import sys

tc=int(sys.stdin.readline())


def drkj(start,num):
    distance=[9999999999999]*(num+1)
    print(graph)
    distance[start]=0
    q=[]
    heapq.heappush(q,(0,start))
    cnt=0
    while q:
        dist,node=heapq.heappop(q)
        if dist>distance[node]:
            continue
        for next in graph[node]:
            newdis=next[1]+dist
            if newdis<distance[next[0]]:
                distance[next[0]]=newdis
                cnt+=1
                heapq.heappush(q,(newdis,next[0]))



    max=0
    for i in distance:
        if i==9999999999999:
            continue
        if i>max:
            max=i


    return cnt,max


for _ in range(tc):
    n,num,start=map(int,sys.stdin.readline().split())
    graph=[[] for _ in range(n+1)]
    for i in range(num):
        a,b,c=map(int,sys.stdin.readline().split())
        graph[b].append((a,c))


    k=drkj(start,n)

    print(k[0],k[1])