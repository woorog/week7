import sys

n=int(sys.stdin.readline())
nums=list(map(int,sys.stdin.readline().split()))

ans=[nums[0],nums[len(nums)-1]]
SP=0
EP=len(nums)-1

while 1:
    prv=EP-SP
    if prv==1:
        break
    LM=abs(nums[SP+1]+nums[EP])

    RM=abs(nums[SP]+nums[EP-1])

    if LM<=RM:
        if LM<=abs(sum(ans)):
            ans=[nums[SP+1],nums[EP]]
        SP+=1
    else:
        if RM<=abs(sum(ans)):
            ans=[nums[SP],nums[EP-1]]
        EP-=1




print(ans[0],ans[1])

