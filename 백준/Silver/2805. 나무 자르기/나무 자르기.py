from collections import deque
                   
tree_num, need_length = map(int, input().split())
tree_list = deque(map(int, input().split()))

start = 0
end = max(tree_list)
  
while start <= end:
    mid = (start + end) // 2
        
    length_sum = 0
    for t in tree_list:
        if t - mid < 0:
            continue
        else:
            length_sum += t-mid
                
    if length_sum >= need_length:
        start = mid + 1

    else:
        end = mid - 1
    
print(end)