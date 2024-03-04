import sys
from collections import deque

R,C=map(int,sys.stdin.readline().split())
#
board=[]

for _ in range(R):
    a=list(map(str,sys.stdin.readline().strip()))
    board.append(a)
#

# print(ord('Z'))
#
# q=deque()
#
# prov=[0]*100
# prov[ord(board[0][0])]=1
# q.append((0,0))
# cnt=0
#
# while q:
#     ny,nx=q.popleft()
#     case=[0,0,0,0]
#     if ny+1<y and prov[ord(board[ny+1][nx])]==0:
#         case[0]=1
#         q.append((ny+1,nx))
#     if ny-1>=0 and prov[ord(board[ny-1][nx])]==0:
#         case[1]=1
#         q.append((ny-1,nx))
#     if nx+1<x and prov[ord(board[ny][nx+1])]==0:
#         case[2]=1
#         q.append((ny,nx+1))
#     if nx-1>=0 and prov[ord(board[ny][nx-1])]==0:
#         case[3]=1
#         q.append((ny,nx-1))
#     if case[0]==1:
#         prov[ord(board[ny+1][nx])]=1
#     if case[1]==1:
#         prov[ord(board[ny-1][nx])]=1
#     if case[1]==1:
#         prov[ord(board[ny][nx+1])]=1
#     if case[1]==1:
#         prov[ord(board[ny][nx-1])]=1
#
#
# for i in range(60,99):
#     if prov[i]==1:
#         cnt+=1

def dfs(y, x, visited, count):
    global max_count
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 상, 하, 좌, 우 이동
    max_count = max(max_count, count)  # 최대 칸 수 갱신

    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        if 0 <= ny < R and 0 <= nx < C and board[ny][nx] not in visited:  # 범위 내부이고, 방문하지 않은 알파벳이라면
            dfs(ny, nx, visited + board[ny][nx], count + 1)  # DFS 탐색

max_count = 0  # 최대 칸 수
dfs(0, 0, board[0][0], 1)  # DFS 탐색 시작, 초기 위치 (0,0), 방문한 알파벳, 칸 수

print(max_count)  # 최대 칸 수 출력