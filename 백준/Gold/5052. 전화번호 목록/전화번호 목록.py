import sys
input = sys.stdin.readline

class Node(object):
    def __init__(self, key, data = None):
        self.key = key
        self.data = data
        self.child = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)
    
    def insert_true(self, string):
        current_node = self.head
        
        for c in string:
            if current_node.data:
                return False
            if c not in current_node.child:
                current_node.child[c] = Node(c)
            current_node = current_node.child[c]
            
        current_node.data = string
        return True

def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = len(array) // 2
    front_arr, pivot_arr, back_arr = [], [], []
    
    for value in array:
        if len(value) < len(array[pivot]):
            front_arr.append(value)
        elif len(value) > len(array[pivot]):
            back_arr.append(value)
        else:
            pivot_arr.append(value)
    if len(front_arr) == 0 and len(back_arr) == 0 and len(pivot_arr) != 0:
        return pivot_arr
    return quick_sort(front_arr) + quick_sort(pivot_arr) + quick_sort(back_arr)

t = int(input())
result = []

for i in range(t):
    n = int(input())
    phone_list = []
    for j in range(n):
        num = input()
        phone_list.append(num[:-1])
    
    phone_list = quick_sort(phone_list)

    phone_trie = Trie()
    flag = True

    
    for number in phone_list:
        if phone_trie.insert_true(number):
            continue
        else:
            result.append("NO")
            flag = False
            break
    
    if flag:
        result.append("YES")
 
for i in result:
    print(i)    