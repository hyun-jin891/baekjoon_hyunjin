import sys
import bisect
input = sys.stdin.readline

N = int(input())
l = list(map(int, input().split()))
process_lis = [l[0]]
dp = [0] * N
dp[0] = 1

for i in range(1, N):
    if l[i] > process_lis[-1]:
        process_lis.append(l[i])
        dp[i] = len(process_lis)
    else:
        index = bisect.bisect_left(process_lis, l[i])
        process_lis[index] = l[i]
        dp[i] = index + 1   

maxLength = max(dp)
maxIndex = dp.index(maxLength)
print(maxLength)
lis = [l[maxIndex]]
difference = 1

for i in range(maxIndex - 1, -1, -1):
    if dp[i] + difference == maxLength:
        lis.append(l[i])
        difference += 1

for i in range(len(lis)):
    print(lis[len(lis) - i - 1], end = " ")