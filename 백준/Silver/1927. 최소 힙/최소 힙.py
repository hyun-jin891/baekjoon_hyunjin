import sys
import heapq
    
input = sys.stdin.readline

N = int(input())
minheap = []
output = []

for i in range(N):
    num = int(input())
    if num == 0:
        if len(minheap) == 0:
            output.append(0)
        else:
            output.append(heapq.heappop(minheap))

    else:
        heapq.heappush(minheap, num)
            
sys.stdout.write("\n".join(map(str, output)))  