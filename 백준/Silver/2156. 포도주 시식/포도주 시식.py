N = int(input())
amount = [0]

for i in range(N):
    amount.append(int(input()))

dp = [0] * (N + 1)
dp[1] = amount[1]
if N > 1:
    dp[2] = amount[1] + amount[2]

for i in range(3, N + 1):
    dp[i] = max(dp[i - 1], amount[i] + amount[i - 1] + dp[i - 3], amount[i] + dp[i - 2])

print(dp[-1])