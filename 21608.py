import copy
import sys

y,x,time=map(int,sys.stdin.readline().split())

board=[]

for _ in range(y):
    board.append(list(map(int,sys.stdin.readline().split())))

print(board)
cboard=[[0]*x for _ in range(y)]
print(cboard)

for i in range(y):
    for k in range(x):
        if board[i][k]>4:
            cnt=0
            temp=int(board[i][k]/5)
            if i+1<y and board[i+1][k] > -1:
                cboard[i+1][k]+=temp
                cnt+=1

            if k+1<x and board[i][k+1] > -1:
                cboard[i][k+1]+=temp
                cnt+=1

            if i-1>=0 and board[i-1][k] > -1:
                cboard[i-1][k]+=temp
                cnt+=1

            if k-1>=0 and board[i][k-1] > -1:
                cboard[i][k-1]+=temp
                cnt+=1

            cboard[i][k]=board[i][k]-temp*cnt+cboard[i][k]
        else:
            cboard[i][k]=board[i][k]+cboard[i][k]



for i in range(y):
    print(cboard[i])

air=[]

for i in range(y):
    for k in range(x):
        if board[i][k]==-1:
            air.append((i,k))

print(air[0][0],air[0][1])

kboard=copy.deepcopy(cboard)
for _ in range(time):
    #보드 클리어 시켜주기
    # kboard[0]=[0]*x
    # kboard[y-1]=[0]*x
    # kboard[air[0][0]]=[0]*x
    # kboard[air[1][0]]=[0]*x
    # for i in range(y):
    #     kboard[i][0]=0
    #     kboard[i][x-1]=0
    # 보드 옮기기
    kboard[0].append(0)
    del kboard[0][0]
    kboard[y-1].append(0)
    del kboard[y-1][0]

    print()

    for i in range(air[0][0]):
        kboard[i+1][0]=cboard[i][0]
        if i-1>=0:
            kboard[i][x-1]=cboard[i+1][x-1]
    for i in range(air[1][0],y):
        if i+1<y:
            kboard[i][0]=cboard[i+1][0]
            kboard[i+1][x-1]=cboard[i][x-1]

    kboard[air[0][0]].insert(0,0)
    del kboard[air[0][0]][x-1]
    kboard[air[1][0]].insert(0,0)
    del kboard[air[1][0]][x-1]

    for i in range(y):
        print(kboard[i])



