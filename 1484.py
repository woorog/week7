import sys

goal=int(sys.stdin.readline())

nums=[]

for i in range(1,int(goal/2+2)):
    nums.append(i**2)


lists=[]
for i in range(len(nums)):
    for k in range(i):
        if nums[i]-nums[k]==goal:
            lists.append(nums[i])
            break
if len(lists)==0:
    print(-1)
else:
    for i in lists:
        print(int(i**0.5))