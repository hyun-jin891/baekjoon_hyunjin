num = int(input())
output = []
n = 0
while n < num:
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            output.append(-1)
            n += 1
            continue
        else:
            output.append(0)
            n += 1
            continue
 
    d = ((x1-x2)**2 + (y1-y2)**2) ** 0.5
    sum_r = r1 + r2
    sub_r = abs(r1 - r2)
    
    if d == sum_r:
        output.append(1)
    elif d < sum_r and d > sub_r:
        output.append(2)
    elif d > sum_r:
        output.append(0)
    
    if d == sub_r:
        output.append(1)
    elif d < sub_r:
        output.append(0)
        
    n += 1
  
for i in output:
    print(i) 