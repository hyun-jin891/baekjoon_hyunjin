import sys
import bisect
input = sys.stdin.readline

N = int(input())
l = list(map(int, input().split()))
process_lis = [l[0]]

for i in range(1, N):
    if l[i] > process_lis[-1]:
        process_lis.append(l[i])
    else:
        index = bisect.bisect_left(process_lis, l[i])
        process_lis[index] = l[i]

print(len(process_lis))