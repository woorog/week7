import copy
import sys

input=sys.stdin.readline

n=int(input())
nums=list(map(int,input().split()))
nums.sort()
cnt=0

for i in range(n):
    testnum=copy.deepcopy(nums)

    del testnum[i]
    SP=testnum[0]
    S=0
    EP=testnum[len(testnum)-1]
    E=len(testnum)-1
    while 1:
        if SP+EP==nums[i]:
            cnt+=1
            break
        if E-S==1:
            break
        if SP+EP>nums[i]:
            E-=1
            EP=testnum[E]
        else:
            S+=1
            SP=testnum[S]
# for i in range(2,n):
#     if nums[0]+nums[i-1]==nums[i]:
#         cnt+=1
#     elif nums[0]+nums[i-1]>nums[i]:
#         for k in range(i-1,-1,-1):
#             if nums[k]+nums[0]==nums[i]:
#                 print(nums[k]+nums[0])
#                 cnt+=1
#                 break
#             elif nums[k]+nums[0]<nums[i]:
#                 break
#     else:
#         for k in range(i-1):
#             if nums[k]+nums[i-1]==nums[i]:
#                 print(nums[k]+nums[i-1])
#                 cnt+=1
#                 break
#             elif nums[k]+nums[i-1]>nums[i]:
#                 break

print(cnt)



