# import sys
#
# n=int(sys.stdin.readline())
# nums=list(map(int,sys.stdin.readline().split()))
#
# ans=n
#
# for size in range(1,n):
#     SP=nums[0]
#     S=0
#     EP=nums[size]
#     E=size
#     newlist=nums[:EP]
#     for i in range(size,n):
#         k=len(set(newlist))
#         if k==size+1:
#             ans+=1
#         del newlist[0]
#         if i+1<n:
#             newlist.append(nums[i+1])
#
# print(ans)
import sys
from collections import defaultdict

num_dict = defaultdict(list)
input = sys.stdin.readline
n = int(input().rstrip())

num_list = list(map(int, input().split()))

ans = 0
start, end = 0, 0
seq = [False for _ in range(1000001)]
while start < n and end < n:
    if not seq[num_list[end]]:      # start부터 end까지 중복 숫자 없으면
        seq[num_list[end]] = True
        end += 1
        ans += (end - start)     # end를 포함하여 만들 수 있는 수열의 개수
    else:
        seq[num_list[start]] = False
        start += 1

print(ans)
