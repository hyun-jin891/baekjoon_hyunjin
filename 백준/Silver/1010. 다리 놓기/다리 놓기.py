T = int(input())
testCase = []

for i in range(T):
    testCase.append(list(map(int, input().split())))

for i in testCase:
    N = i[0]
    M = i[1]
    dp = [[0] * (M + 1) for k in range(N + 1)]
    
    for j in range(1, N + 1):
        for k in range(1, M + 1):
            if j == 1:
                dp[j][k] = k
                continue
            
            if j > k:
                dp[j][k] = 0
                continue
            
            if j == k:
                dp[j][k] = 1
                continue
            
            dp[j][k] = dp[j - 1][k - 1] + dp[j][k - 1]
        
    
    print(dp[-1][-1])