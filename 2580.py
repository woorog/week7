# import sys
# from collections import deque
#
# board=[]
# for _ in range(9):
#     board.append(list(map(int,sys.stdin.readline().split())))
#
#
#
# q=deque()
# for i in range(9):
#     for k in range(9):
#         if board[i][k]==0:
#             q.append((i,k))
#
#
#
# def provy(y, x):
#     cnt=0
#     sums=45
#     for i in range(9):
#         if cnt>1:
#             return 0
#         if board[i][x]==0:
#             cnt+=1
#         sums-=board[i][x]
#     if cnt==1:
#         return sums
#     else:
#         return 0
#
#
# while q:
#     y,x=q.popleft()
#     k=provy(y,x)
#
#     if k>0:
#         board[y][x]=k
#         # print('1',y,x)
#         # print(board[y][x])
#     elif board[y].count(0)==1:
#         board[y][x]=45-sum(board[y])
#         # print('2',y,x)
#     else:
#         startx=int(x/3)*3
#         starty=int(y/3)*3
#         # print('3',y,x)
#         sums=45
#         prv=0
#         for i in range(starty,starty+3):
#             for k in range(startx,startx+3):
#                 if board[i][k]==0:
#                     prv+=1
#                 sums-=board[i][k]
#         if prv==1:
#             board[y][x]=sums
#         else:
#             q.append((y,x))
#
#
# for i in range(9):
#     for k in range(9):
#         print(board[i][k],end=' ')
#     print()
#
import sys

board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

empty_cells = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]

def is_valid(y, x, num):
    # Check row
    if num in board[y]:
        return False
    # Check column
    if num in [board[i][x] for i in range(9)]:
        return False
    # Check subgrid
    start_row, start_col = 3 * (y // 3), 3 * (x // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True

def solve_sudoku():
    if not empty_cells:
        return True

    y, x = empty_cells[0]
    for num in range(1, 10):
        if is_valid(y, x, num):
            board[y][x] = num
            empty_cells.pop(0)
            if solve_sudoku():
                return True
            board[y][x] = 0
            empty_cells.insert(0, (y, x))
    return False

solve_sudoku()

for row in board:
    print(*row)


