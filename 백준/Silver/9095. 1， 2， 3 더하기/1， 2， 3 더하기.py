n = int(input())
Input = []

for i in range(n):
    Input.append(int(input()))

dp = [0] * (1 + max(Input))
dp[0] = 1
dp[1] = 1

if max(Input) > 1:
    dp[2] = 2

for i in range(3, len(dp)):
    dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

for i in Input:
    print(dp[i])