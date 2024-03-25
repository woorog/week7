import copy
import sys

y,x,time=map(int,sys.stdin.readline().split())

board=[[] for _ in range(y)]
for k in range(y):
    temp=list(sys.stdin.readline().strip())
    for i in temp:
        if i =='.':
            board[k].append(0)
        else:
            board[k].append(2)

dis=(0,1),(1,0),(-1,0),(0,-1)

while time>1:
    time-=1
    for i in range(y):
        for k in range(x):
            board[i][k]+=1
    cboard=copy.deepcopy(board)
    for i in range(y):
        for k in range(x):
            if board[i][k]==4:
                cboard[i][k]=0
                for dy,dx in dis:
                    if 0<=i+dy<y and 0<=k+dx<x:
                        cboard[dy+i][dx+k]=0

    board=cboard
    # print(board)

for i in range(y):
    for k in board[i]:
        if k>0:
            print('O',end='')
        else:
            print('.',end='')
    print()



def asd():
    print(1)
# print(board)


print(asd())
