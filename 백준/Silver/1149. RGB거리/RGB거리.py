house_n = int(input())
dp = [[0]*3 for i in range(house_n+1)]
h_price = []

for i in range(house_n):
    R, G, B = map(int, input().split())
    h_price.append([R, G, B])

for i in range(1, len(dp)):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + h_price[i-1][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + h_price[i-1][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + h_price[i-1][2]

print(min(dp[house_n]))