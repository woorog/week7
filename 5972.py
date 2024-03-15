import heapq
import sys

n,m=map(int,sys.stdin.readline().split())
start=1
INF=int(1e9)
distance=[INF]*(n+1)
graph=[[]for _ in range(n+1)]

for i in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    graph[a].append((b,c))
    graph[b].append((a,c))


def dijk(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0

    while q:
        dist,node=heapq.heappop(q)
        if distance[node]<dist:   #갱신된 정보보다 클 경우
            continue
        for next in graph[node]:
            cost=distance[node]+next[1]   #next1에는 거리정보
            if cost<distance[next[0]]:
                distance[next[0]]=cost
                heapq.heappush(q,(cost,next[0]))


dijk(start)

print(distance[n])
