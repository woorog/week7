board = [0] * 41
n = int(input())
arr = list(map(int,input().split()))
for num in arr:
    board[num] += 1
prev_cnt = 2
flag = False
for cnt in board:
    if cnt > prev_cnt:
        flag = True
        break
    prev_cnt = cnt

if flag:
    print(0)
else:
    result = 2**(board.count(2) + (1 in board))
    print(result)