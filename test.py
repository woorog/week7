import sys
from collections import deque

x, y = map(int, sys.stdin.readline().split())

board = []
for _ in range(y):
    a = str(sys.stdin.readline())
    board.append(list(a))

visited = [[0] * x for _ in range(y)]
block = [[0] * x for _ in range(y)]
q = deque()
q.append((0, 0))
visited[0][0] = 1

# 방향 이동을 위한 델타값: 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    cx, cy = q.popleft()  # 현재 위치
    if cx == x - 1 and cy == y - 1:
        break
    for i in range(4):
        nx, ny = cx + dx[i], cy + dy[i]
        if 0 <= nx < x and 0 <= ny < y and visited[ny][nx] == 0:
            if board[ny][nx] == '0':
                block[ny][nx] = block[cy][cx]
                visited[ny][nx] = 1
                q.appendleft((nx, ny))
            elif board[ny][nx] == '1':
                block[ny][nx] = block[cy][cx] + 1
                visited[ny][nx] = 1
                q.append((nx, ny))

print(block[y - 1][x - 1])