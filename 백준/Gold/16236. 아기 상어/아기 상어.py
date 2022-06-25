from collections import deque

def init_index_shark(l):
    c = 0
    for i in l:
        for j in i:
            if j == 9:
                return i.index(j), c
        c += 1

n = int(input())
ocean = []

for i in range(n):
    l = input().split()
    l2 = []
    for j in l:
        l2.append(int(j))
    ocean.append(l2)

def shark_bfs(graph, x, y, size, eat_count):
    dx = [0, -1, 1, 0]
    dy = [-1, 0, 0, 1]
    distance_map = [[0]*n for i in range(n)]
    need_v = deque()
    need_v.append([x, y])
    output = deque()
    
    while need_v:
        start_x, start_y = need_v.popleft()
        
        for i in range(4):
            explo_x = start_x + dx[i]
            explo_y = start_y + dy[i]
            if explo_x < 0 or explo_y < 0 or explo_x >= n or explo_y >= n:
                continue
            if graph[explo_y][explo_x] > size:
                continue
            if graph[explo_y][explo_x] != 0 and graph[explo_y][explo_x] < size and [explo_x, explo_y] not in output:
                distance_map[explo_y][explo_x] = distance_map[start_y][start_x] + 1
                output.append([explo_x, explo_y])
                
            if distance_map[explo_y][explo_x] == 0 and [explo_x, explo_y] not in output:
                need_v.append([explo_x, explo_y])
                distance_map[explo_y][explo_x] = distance_map[start_y][start_x] + 1
    
    if len(output) == 0:
        return 0, [x, y], eat_count
    
    min_distance = distance_map[output[0][1]][output[0][0]]
    out_x, out_y = output.popleft()
    
    for i in range(len(output)):
        o_x, o_y = output.popleft()
        if distance_map[o_y][o_x] < min_distance:
            min_distance = distance_map[o_y][o_x]
            out_x = o_x
            out_y = o_y
        if distance_map[o_y][o_x] == min_distance:
            if o_y < out_y:
                out_x = o_x
                out_y = o_y
                
            elif o_y == out_y:
                if o_x < out_x:
                    out_x = o_x
                    out_y = o_y
        
    graph[out_y][out_x] = 0
    eat_count += 1
    return distance_map[out_y][out_x], [out_x, out_y], eat_count

i_x, i_y = init_index_shark(ocean)
ocean[i_y][i_x] = 0
total_time = 0
shark_size = 2
e_count = 0

while True:
    add_time, new_coord, e_count = shark_bfs(ocean, i_x, i_y, shark_size, e_count)
    if add_time == 0:
        break
    total_time += add_time
    i_x = new_coord[0]
    i_y = new_coord[1]
    
    if e_count == shark_size:
        shark_size += 1
        e_count = 0
        continue


print(total_time) 