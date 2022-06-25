from collections import deque

def search(minimum_distance, array):
    wifi = 1
    i = 0
    first = array[0]
    
    while i < len(array)-1:
        i += 1      
        distance = array[i] - first
        if distance < minimum_distance:
            continue
        else:
            wifi += 1
            if wifi == WIFI_num:
                return True
            
            first = array[i]
            continue
        
    return False   

house_num, WIFI_num = map(int, input().split())
house_position = deque([int(input()) for i in range(house_num)])
house_position = sorted(house_position)

end = house_position[-1] - house_position[0]
start = min(deque([(house_position[i+1])-(house_position[i]) for i in range(len(house_position)-1)]))


while start <= end:
    mid = (start + end) // 2
    
    
    if search(mid, house_position):
        start = mid + 1
        
    else:
        end = mid - 1

print(end)