C, N = map(int, input().split())  # C: 목표 고객 수, N: 도시의 개수
dp = [float('inf')] * (C+100)  # 고객 수 C를 달성하기 위한 최대 비용을 고려하여 초기화
dp[0] = 0  # 0명의 고객을 달성하는데 필요한 비용은 0

for _ in range(N):
    cost, customers = map(int, input().split())
    for i in range(customers, C+100):
        dp[i] = min(dp[i], dp[i-customers] + cost)

# 목표 고객 수 C를 달성할 수 있는 최소 비용을 찾습니다.
for i in range(C, C+100):
    if dp[i] < float('inf'):
        print(dp[i])
        break