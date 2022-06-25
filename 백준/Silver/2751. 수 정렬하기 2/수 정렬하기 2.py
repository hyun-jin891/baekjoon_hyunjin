from collections import deque

n = int(input())
array = deque()

for i in range(n):
    array.append(int(input()))

s_array = sorted(array)

for i in s_array:
    print(i)