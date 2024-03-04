import sys
from collections import deque

n,case=map(int,sys.stdin.readline().split())

graph = {i: {} for i in range(1, n+1)}

for _ in range(n-1):
    a, b, dis = map(int,sys.stdin.readline().split())

    if b not in graph[a]:
        graph[a][b] = dis
    if a not in graph[b]:
        graph[b][a] = dis


def bfs(g, s, e):
    visited=[0]*(n+1)
    q=deque()
    q.append(s)
    visited[s]=1

    # for i in g[1]:
    #     print(i)
    while q:
        now=q.pop()
        if now==e:
            break
        for i in g[now]:
            if visited[i]==0:
                visited[i]=visited[now]+g[now][i]
                q.append(i)


    print(visited[e]-1)


for _ in range(case):
    start,end=map(int,sys.stdin.readline().split())
    bfs(graph,start,end)