import sys

n=int(sys.stdin.readline())

dp= [0] * (n + 6)

for i in range(len(dp)):
    dp[i]= i + 1

for i in range(n):
    dp[i+3]=max(dp[i]*2,dp[i+3])
    dp[i+4]=max(dp[i]*3,dp[i+4])
    dp[i+5]=max(dp[i]*4,dp[i+5])

print(dp[n-1])