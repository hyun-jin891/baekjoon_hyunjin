def fibo(n):
    f = 0
    s = 1
    c = 0
    num = 0
    if n == 1:
        return 1
    elif n == 0:
        return 0
    
    while num < n-1:
        c = s + f
        f = s
        s = c
        num += 1
    
    return c

class N:
    def __init__(self, n):
        if n == 0:
            self.zero = 1
            self.one = 0
        else:
            self.zero = fibo(n - 1)
            self.one = fibo(n)
        
num = int(input())
output = []
for i in range(num):
    t = int(input())
    o = N(t)
    output.append(o)
        

for i in output:
    print(i.zero, i.one)