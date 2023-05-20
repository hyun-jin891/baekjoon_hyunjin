N = int(input())
l = [None] * 501
maxIndex = 0

for i in range(N):
    index, pair = map(int, input().split())
    if index >= maxIndex:
        maxIndex = index
    l[index] = pair

dp = [0] * (maxIndex + 1)

for i in range(1, maxIndex + 1):
    if l[i] == None:
        dp[i] = dp[i-1]
        continue
    
    dp[i] = 1
    
    for j in range(1, i + 1):
        if l[j] == None:
            continue
        if l[i] > l[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N-max(dp))   