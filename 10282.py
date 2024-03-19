# import heapq
# import sys
#
# tc=int(sys.stdin.readline())
#
#
# def drkj(start,num):
#     distance=[9999999999999]*(num+1)
#     print(graph)
#     distance[start]=0
#     q=[]
#     heapq.heappush(q,(0,start))
#     cnt=0
#     while q:
#         dist,node=heapq.heappop(q)
#         if dist>distance[node]:
#             continue
#         for next in graph[node]:
#             newdis=next[1]+dist
#             if newdis<distance[next[0]]:
#                 distance[next[0]]=newdis
#                 cnt+=1
#                 heapq.heappush(q,(newdis,next[0]))
#
#
#
#     max=0
#     for i in distance:
#         if i==9999999999999:
#             continue
#         if i>max:
#             max=i
#
#     print(distance)
#     return cnt,max
#
#
# for _ in range(tc):
#     n,num,start=map(int,sys.stdin.readline().split())
#     graph=[[] for _ in range(n+1)]
#     for i in range(num):
#         a,b,c=map(int,sys.stdin.readline().split())
#         graph[a].append((b,c))
#         graph[b].append((a,c))
#
#     k=drkj(start,n)
#
#     print(k[0],k[1])

import heapq
import sys

# input 대신 예제 입력으로 대체하여 테스트합니다.
# tc = int(sys.stdin.readline().strip())
tc = int(input().strip())  # 테스트 케이스 개수

def dijkstra(start, n):
    distance = [float('inf')] * (n + 1)
    distance[start] = 0
    q = [(0, start)]  # (거리, 노드)

    while q:
        dist, node = heapq.heappop(q)
        if dist > distance[node]:
            continue
        for next_node, time in graph[node]:
            new_dist = dist + time
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heapq.heappush(q, (new_dist, next_node))

    infected = [d for d in distance if d != float('inf')]
    return len(infected), max(infected)

for _ in range(tc):
    # n, d, start = map(int, sys.stdin.readline().split())
    n, d, start = map(int, input().split())  # 컴퓨터 개수, 의존성 개수, 해킹당한 컴퓨터 번호
    graph = [[] for _ in range(n + 1)]
    for _ in range(d):
        # a, b, s = map(int, sys.stdin.readline().split())
        a, b, s = map(int, input().split())  # a가 b를 의존, b가 감염되면 s초 후 a도 감염
        graph[b].append((a, s))  # b -> a 의존성 추가

    infected_count, last_infected_time = dijkstra(start, n)
    print(infected_count, last_infected_time)
