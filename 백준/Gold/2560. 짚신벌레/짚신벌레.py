a, b, d, N = map(int, input().split())
dpForNum = [0] * (N + 1)
dpForNum[0] = 1
dpForBorn = [0] * (N + 1)
dpForBorn[0] = 1
sumL = [0] * (N + 1)
sumL[0] = 1

for i in range(1, N + 1):
    if i >= a:
        if i >= b - 1:
            dpForBorn[i] = (sumL[i - a] - sumL[i - b]) % 1000
         
        else:
            dpForBorn[i] = sumL[i - a] % 1000
             
    if i >= d:
        dpForNum[i] = (dpForNum[i - 1] + dpForBorn[i] - dpForBorn[i - d]) % 1000
    else:
         dpForNum[i] = (dpForNum[i - 1] + dpForBorn[i]) % 1000
    
    sumL[i] = (sumL[i - 1] + dpForBorn[i]) % 1000

print(dpForNum[-1])