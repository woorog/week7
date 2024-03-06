import sys
from collections import deque

tc=int(sys.stdin.readline())

board=[]
for _ in range(11):
    board.append(list(map(int,sys.stdin.readline().split())))

print(board)
q=deque()
for i in board[0]:
    if i != 0:
        q.append(i)
#
# while q:
#     dp=q.popleft()
#     for i in
# print(q)
#
