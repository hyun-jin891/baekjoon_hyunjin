class Circle:
    def __init__(self, cx, cy, r):
        self.cx = cx
        self.cy = cy
        self.r = r
    
    def check(self, x, y):
        if (x - self.cx)**2 + (y - self.cy)**2 <= (self.r)**2:
            return 1
        else:
            return 0

N = int(input())
output = []
n = 0

while n < N:
    x1, y1, x2, y2 = map(int, input().split())
    num = int(input())
    sum = 0

    for i in range(num):
        Cx, Cy, R = map(int, input().split())
        circle = Circle(Cx, Cy, R)
        if circle.check(x1, y1) == 1 and circle.check(x2, y2) == 1:
            continue
        else:
            sum += circle.check(x1, y1)
            sum += circle.check(x2, y2)
        
    output.append(sum)
    n += 1

for i in output:
    print(i)