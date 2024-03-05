import sys

time,jump=map(int,sys.stdin.readline().split())

fb=list(sys.stdin.readline().strip())
sb=list(sys.stdin.readline().strip())

dpa=[9999]*time
dpb=[9999]*time
if fb[0]=='1':
    dpa[0]=0
if sb[0]=='1':
    dpb[0]=0
print(fb)

for i in range(time):
    # if i>max(max(dpa),max(dpb)):
    #     break


    if i+1<time and fb[i+1] == '1':
        dpa[i+1]=min(dpa[i+1],dpa[i]+1)
    if i+1<time and sb[i+1] == '1':
        dpb[i+1]=min(dpb[i+1],dpb[i]+1)


    if i-1>0 and fb[i-1]=='1' :
        dpa[i-1]=min(dpa[i-1],dpa[i]+1)
    if i-1>0 and sb[i-1]=='1' :
        dpb[i-1]=min(dpb[i-1],dpb[i]+1)
    if i+jump<time and sb[i+jump]=='1' :
        dpb[i+jump]=min(dpa[i]+1,dpb[i+jump])

    if i+jump<time and fb[i+jump]=='1':
        dpa[i+jump]=min(dpb[i]+1,dpa[i+jump])


print(dpa)
print(dpb)

