N = int(input())
life_l = [0]
greeting_l = [0]
life_l.extend(input().split())
greeting_l.extend(input().split())

for i in range(1, len(life_l)):
    life_l[i] = int(life_l[i])

for i in range(1, len(greeting_l)):
    greeting_l[i] = int(greeting_l[i])
    
dp = [[0] * 101 for i in range(N + 1)]


for i in range(1, len(dp)):
    for j in range(1, 101):
        if life_l[i] < j:
            if greeting_l[i] + dp[i - 1][j - life_l[i]] > dp[i - 1][j]:
                dp[i][j] = greeting_l[i] + dp[i - 1][j - life_l[i]]
            else:
                dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = dp[i - 1][j]
                
print(dp[N][100])   