from collections import deque
n = int(input())
ox = deque()

for i in range(n):
    ox.append(input())

for i in ox:
    dp = [0] * (len(i)+1)
    for j in range(1, len(dp)):
        if i[j-1] == 'X':
            dp[j] = dp[j-1]
        else:
            sum = 0
            for k in range(j-1, -1, -1):
                if i[k] == 'X':
                    break
                sum += 1
                    
            dp[j] = dp[j-1] + sum
    print(dp[-1])