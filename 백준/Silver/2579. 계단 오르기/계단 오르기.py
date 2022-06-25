n = int(input())
dp = [0]*(n+1)
score = [0]

for i in range(n):
    score.append(int(input()))
    
for i in range(1, len(dp)):
    if i >= 3:
        dp[i] = max(dp[i-3] + score[i-1] + score[i], dp[i-2]+score[i])
        continue
    
    else:
        dp[i] = dp[i-1] + score[i]

print(dp[-1])   