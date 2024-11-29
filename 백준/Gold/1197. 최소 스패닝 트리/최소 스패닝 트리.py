class edge:
    def __init__(self, weight, node1, node2):
        self.weight = weight
        self.node1 = node1
        self.node2 = node2
        

def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l].weight < high_arr[h].weight:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr

def find_set(x, parent):
    if parent[x] == x:
        return x
    
    parent[x] = find_set(parent[x], parent)
    return parent[x]

def union_set(x, y, parent, rank):
    rootX = find_set(x, parent)
    rootY = find_set(y, parent)
    
    if rootX == rootY:
        return False
    
    if rank[rootX] < rank[rootY]:
        rootX, rootY = rootY, rootX
    
    parent[rootY] = rootX
    rank[rootX] += rank[rootY]
    return True


n, m = list(map(int, input().split()))
edges = [None for i in range(m)]
parent = [i for i in range(n)]
rank = [1 for i in range(n)]

for i in range(m):
    node1, node2, w = list(map(int, input().split()))
    edges[i] = edge(w, node1 - 1, node2 - 1)

sorted_edges = merge_sort(edges)



res = 0

for i in range(len(sorted_edges)):
    curEdge = sorted_edges[i]
    flag = union_set(curEdge.node1, curEdge.node2, parent, rank)
    if flag == True:
        res += curEdge.weight


print(res)