import copy
import sys
from collections import deque

n,small,big=map(int,sys.stdin.readline().split())

board=[]

for i in range(n):
    board.append(list(map(int,sys.stdin.readline().split())))




sumlist=[0]*10000000
now=0
dis=[(0,1),(1,0),(0,-1),(-1,0)]
cnt=0
def move(i, k,now):
    temp=now
    q=deque()
    q.append((i,k))
    count=1
    while q:
        y,x=q.popleft()
        for dy,dx in dis:
            dy+=y
            dx+=x
            if 0<=dy<n and 0<=dx<n and visited[dy][dx]==0 and  small<=abs(board[y][x] - board[dy][dx])<=big :
                visited[dy][dx]=temp
                sumlist[temp]+=board[dy][dx]
                count+=1
                q.append((dy,dx))


    one=int(sumlist[temp]/count)
    for i in range(n):
        for k in range(n):
            if visited[i][k]==now:
                board[i][k]=one

    print(board)





while True:
    ans=0
    visited=[[0]*n for _ in range(n)]
    cboard=copy.deepcopy(board)
    for i in range(n):
        for k in range(n):
            for dy,dx in dis:
                if 0<=i+dy<n and 0<=k+dx<n and visited[i+dy][k+dx]==0  and  small<=abs(board[i][k] - board[i+dy][k+dx])<=big :
                    now+=1
                    visited[i][k]=now
                    sumlist[now]+=board[i][k]
                    move(i,k,now)
                    ans=1
                else:
                    visited[i][k]=-1
    if ans==0:
        break
    cnt+=1



# print(sumlist)
# print(now)
print(cnt)
