import sys
#import sys
#sys.stdin = open("input.txt", "r")
tc= int(input())

for i in range(tc):
    a,b,c=map(int, input().split())
    cnt=0
    if c<3 or b<2:
        print(f"#{i}",-1)
    elif a<b<c:
        print(f"#{i}",0)
    else:
        while b>=c:
            b-=1
            cnt+=1
        while a>=b:
            a-=1
            cnt+=1
        print(f"#{i}",cnt)
