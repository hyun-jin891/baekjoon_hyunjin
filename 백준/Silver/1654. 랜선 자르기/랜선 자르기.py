K, N = map(int, input().split())
line = [int(input()) for i in range(K)]

start = 1
end = max(line)

while start <= end:
    mid = (start + end) // 2
    sum = 0
    for l in line:
        sum += (l // mid)
    
    if sum >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)