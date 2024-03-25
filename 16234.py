import sys
from collections import deque

n,small,big=map(int,sys.stdin.readline().split())

board=[]

for i in range(n):
    board.append(list(map(int,sys.stdin.readline().split())))



print(board)

sumlist=[0]*n*n
now=0
dis=[(0,1),(1,0),(0,-1),(-1,0)]

def move(i, k,now):
    temp=now
    q=deque()
    q.append((i,k))
    while q:
        y,x=q.popleft()
        for dy,dx in dis:
            dy+=y
            dx+=x
            if 0<=dy<n and 0<=dx<n and visited[dy][dx]==0 and  small<=abs(board[y][x] - board[dy][dx])>=big :
                visited[dy][dx]=temp
                sumlist[temp]+=visited[dy][dx]
                q.append((dy,dx))





visited=[[0]*n for _ in range(n)]
# while sum(sumlist)==0:

    for i in range(n):
        for k in range(n):
            for dy,dx in dis:
                if 0<=i+dy<n and 0<=k+dx<n and visited[i+dy][k+dx]==0:
                    now+=1
                    visited[i][k]=now
                    sumlist[now]+=board[i][k]
                    move(i,k,now)
                else:
                    visited[i][k]=-1


    print(sumlist)
