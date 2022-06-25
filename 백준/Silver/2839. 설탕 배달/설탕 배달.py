from collections import deque

n = int(input())
five = deque()
f_i = 1

while 5 * f_i <= n:
    five.append(5 * f_i)
    f_i += 1

flag = False
for i in range(len(five)):
    f = five[len(five)-i-1]
    if n == f:
        print(len(five)-i)
        flag = True
        break
    if (n - f) % 3 == 0:
        sum = len(five)-i + (n - f) / 3
        print(int(sum))
        flag = True
        break
    else:
        continue

if flag == False:
    if n % 3 == 0:
        print(int(n/3))
    else:
        print(-1)        
    