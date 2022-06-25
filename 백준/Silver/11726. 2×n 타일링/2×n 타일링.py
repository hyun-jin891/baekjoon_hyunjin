n = int(input())
dp = [0]*(n+1)
fibo = [0] * (n+1)
fibo[1] = 1
dp[0] = 1

for i in range(2, len(fibo)):
    fibo[i] = fibo[i-2] + fibo[i-1]

for i in range(1, len(dp)):
    dp[i] = dp[i-1] + fibo[i-1]

print(dp[-1]%10007)