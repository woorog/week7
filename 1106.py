import sys

hu,city=map(int,sys.stdin.readline().split())

dp=[0]*(hu+2)

for _ in range(city):
    cost,p=map(int,sys.stdin.readline().split())
    for i in range(1,hu+2):
        if i>=cost:
            dp[i]=max(dp[i-cost]+p,dp[i])
            if dp[i]<dp[i-1]:
                dp[i]=dp[i-1]
ans=0
for i in dp:
    if i>=hu:
        break
    ans+=1
print(ans)

