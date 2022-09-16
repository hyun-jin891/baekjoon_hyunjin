import sys

input = sys.stdin.readline

N, S, M = map(int, input().split())
v = [0]
v.extend(list(map(int, input().split())))

dp = [[0] * (M + 1) for i in range(N + 1)]


for i in range(1, len(dp)):
    for j in range(M + 1):
        if i == 1:
            add = j - v[i]
            sub = j + v[i]
            max1 = 0
            max2 = 0
            
            if add < 0:
                add = 0
            if sub > M:
                sub = M
            
            if add < S:
                max1 = -1
            else:
                max1 = S + v[i]
                if max1 > j:
                    max1 = -1    
            
            if sub < S:
                max2 = -1
            else:
                max2 = S - v[i]
                if max2 > j:
                    max2 = -1

            dp[i][j] = max(max1, max2)
        
        else:
            add = j - v[i]
            sub = j + v[i]
            max1 = 0
            max2 = 0
            
            if add < 0:
                add = 0
            if sub > M:
                sub = M
            
            if dp[i - 1][add] == -1:
                max1 = -1
            else:
                max1 = dp[i - 1][add] + v[i]
                if max1 > j:
                    max1 = -1    
            
            if dp[i - 1][sub] == -1:
                max2 = -1
            else:
                max2 = dp[i - 1][sub] - v[i]
                if max2 > j:
                    max2 = -1 

            dp[i][j] = max(max1, max2)
     
        
print(dp[-1][-1])   