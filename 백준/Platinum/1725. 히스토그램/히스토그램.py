import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N = int(input()[:-1])

def init_tree(start, end, index, t, h):
    if start == end:
        t[index] = start
        return start
    
    mid = (start + end) // 2
    index_left = init_tree(start, mid, index * 2, t, h)
    index_right = init_tree(mid + 1, end, index * 2 + 1, t, h)
    
    if h[index_left] <= h[index_right]:
	    t[index] = index_left
	    return index_left
    else:
	    t[index] = index_right
	    return index_right

def internal_min(start, end, index, left, right, t, h):
    if left > end or right < start:
        return -1
    if left <= start and right >= end:
        return index
    
    mid = (start + end) // 2
    index_left = internal_min(start, mid, index * 2, left, right, t, h)
    index_right = internal_min(mid + 1, end, index *2 + 1, left, right, t, h)
    
    if index_left == -1 and index_right == -1:
        return -1
    elif index_left == -1:
        return index_right
    elif index_right == -1:
        return index_left
    elif h[t[index_left]] <= h[t[index_right]]:
        return index_left
    else:
        return index_right

def Area(start, end, index, t, h):
    minHeight = h[t[index]]
    if start >= end:
        return minHeight
        
    currentMaxArea = minHeight * (end - start + 1)
    
    if start > t[index] - 1:
        leftMinIndex = start
    else:
        leftMinIndex = internal_min(1, N, 1, start, t[index] - 1, t, h)
    
    if end < t[index] + 1:
        rightMinIndex = end
    else:
        rightMinIndex = internal_min(1, N, 1, t[index] + 1, end, t, h)
    
    leftMaxArea = Area(start, t[index] - 1, leftMinIndex, t, h)

    rightMaxArea = Area(t[index] + 1, end, rightMinIndex, t, h)
    return max(currentMaxArea, leftMaxArea, rightMaxArea)    
    

input = sys.stdin.readline

histogram = [0]
for i in range(N):
    histogram.append(int(input()[:-1]))

tree = [0] * (len(histogram) * 4)
init_tree(1, N, 1, tree, histogram)

print(Area(1, N, 1, tree, histogram))   
