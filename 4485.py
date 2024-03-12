import heapq
import sys


def dijkstra(maze, start):
    rows = len(maze)
    cols = len(maze[0])

    dis=[0]*rows

    dis[start[0]][start[1]]=0
    q=[(0,start)]

    while q:
        cd,(r,c)=heapq.heappop(q)

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr,nc=r+dr,c+dc

            if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                continue
            nd=cd+maze[nr][nc]
            if nd<dis[nr][nc]:
                dis[nr][nc]=nd
                heapq.heappush(q,)



    # 시작 지점부터의 최단 경로를 저장하는 배열
    distance = [[float('inf')] * cols for _ in range(rows)]
    distance[start[0]][start[1]] = 0

    # 우선순위 큐 생성
    priority_queue = [(0, start)]

    while priority_queue:
        now_dis, (row, col) = heapq.heappop(priority_queue)

        # 현재 위치에서 인접한 상하좌우 칸들을 확인
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = row + dr, col + dc
            # 미로 범위를 벗어나는 경우 무시
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                continue
            # 이동 가능한 경우에만 경로를 업데이트
            new_dis = now_dis + maze[nr][nc]  # 이동 비용을 고려하여 업데이트
            if new_dis < distance[nr][nc]:
                distance[nr][nc] = new_dis
                heapq.heappush(priority_queue, (new_dis, (nr, nc)))


    # while priority_queue:
    #     now_dis, (row, col) = heapq.heappop(priority_queue)
    #
    #     # 현재 위치에서 인접한 상하좌우 칸들을 확인
    #     for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    #         nr, nc = row + dr, col + dc
    #         # 미로 범위를 벗어나는 경우 무시
    #         if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
    #             continue
    #         # 이동 가능한 경우에만 경로를 업데이트
    #         if maze[nr][nc] == 0:
    #             new_dis = now_dis + 1
    #             if new_dis < distance[nr][nc]:
    #                 distance[nr][nc] = new_dis
    #                 heapq.heappush(priority_queue, (new_dis, (nr, nc)))

    return distance

# 예제 미로


# 시작점
start_point = (0, 0)
count=0
while 1:
    count+=1
    lens=int(sys.stdin.readline())
    if lens==0:
        break
    maze = []
    for _ in range(lens):
        maze.append(list(map(int,sys.stdin.readline().split())))
    shortest_distances = dijkstra(maze, start_point)
    print(f"Problem {count}:",shortest_distances[lens-1][lens-1]+maze[0][0])

    print()

# 다익스트라 알고리즘 호출
# shortest_distances = dijkstra(maze, start_point)
#
# # 결과 출력
# print("시작 지점으로부터의 최단 거리:")
# for row in range(len(maze)):
#     for col in range(len(maze[0])):
#         print(shortest_distances[row][col], end=" ")
#     print()
#

