seq = input()
base_l = []
for i in seq:
    base_l.append(i)

dp = [[0 for i in range(len(base_l))] for j in range(len(base_l))]

for i in range(len(base_l) - 2, -1, -1):
    rowBase = base_l[i]
    for j in range(0, len(base_l)):
        columnBase = base_l[j]
        if i >= j:
            dp[i][j] = 0
            continue
        if rowBase == 't' or rowBase == 'c':
            dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
            continue
        if rowBase == 'g' and columnBase == 't':
            maxValue = dp[i][j-1]
            for k in range(i + 1, j):
                if base_l[k] == 'c':
                    for l in range(k + 1, j):
                        if base_l[l] == 'a':
                            if maxValue < dp[i][k] + dp[l][j]:
                                maxValue = dp[i][k] + dp[l][j]
                                break
            dp[i][j] = max(maxValue, dp[i+1][j])
            continue
        
        if rowBase == 'a' and columnBase == 'c':
            maxValue = dp[i][j-1]
            for k in range(i + 1, j):
                if base_l[k] == 't':
                    for l in range(k + 1, j):
                        if base_l[l] == 'g':
                            if maxValue < dp[i][k] + dp[l][j]:
                                maxValue = dp[i][k] + dp[l][j]
                                break
            dp[i][j] = max(maxValue, dp[i+1][j])
            continue 
        
        if rowBase == 'a' and columnBase == 't':
            maxValue1 = dp[i][j-1]
            maxValue2 = dp[i][j-1]
            for k in range(i + 1, j):
                if base_l[k] == 't':
                    for l in range(k + 1, j):
                        if base_l[l] == 'a':
                            if maxValue1 < dp[i][k] + dp[l][j]:
                                maxValue1 = dp[i][k] + dp[l][j]
                                break
                            
            for k in range(j, i - 1, -1):
                if base_l[k] == 'a':
                    if maxValue2 < dp[k][j] + dp[i][k-1]:
                        maxValue2 = dp[k][j] + dp[i][k-1]
                        break
                    
            dp[i][j] = max(dp[i + 1][j - 1] + 2, maxValue1, maxValue2, dp[i+1][j])
            continue
        
        if rowBase == 'g' and columnBase == 'c':
            maxValue1 = dp[i][j-1]
            maxValue2 = dp[i][j-1]
            for k in range(i + 1, j):
                if base_l[k] == 'c':
                    for l in range(k + 1, j):
                        if base_l[l] == 'g':
                            if maxValue1 < dp[i][k] + dp[l][j]:
                                maxValue1 = dp[i][k] + dp[l][j]
                                break
            for k in range(j, i - 1, -1):
                if base_l[k] == 'g':
                    if maxValue2 < dp[k][j] + dp[i][k-1]:
                        maxValue2 = dp[k][j] + dp[i][k-1]
                        break
            dp[i][j] = max(dp[i + 1][j - 1] + 2, maxValue1, maxValue2, dp[i+1][j])
            continue
        
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
            continue

if len(base_l) == 0:
    print(0)
else:
    print(dp[0][len(base_l)-1]) 