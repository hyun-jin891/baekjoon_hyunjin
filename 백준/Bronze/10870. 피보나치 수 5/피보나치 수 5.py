n = int(input())
dp = [0] * (n+1)
if n >= 1:
    dp[1] = 1
for i in range(2, len(dp)):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[-1])