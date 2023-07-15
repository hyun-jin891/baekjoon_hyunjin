import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data = None):
        self.data = data
        self.child = {}
        
    def DFS(self, node, depth = -2):
        if node == None:
            return
        if node.data != None:
            print("-" * depth + node.data)
        
        for key in node.child:
            self.DFS(node.child[key], depth + 2)
            
class Tree:
    def __init__(self):
        self.head = Node()
    
N = int(input())
tree = Tree()

for i in range(N):
    l = input().split()
    current_node = tree.head
    for j in range(1, int(l[0]) + 1):
        if l[j] in current_node.child:
            current_node = current_node.child[l[j]]
            continue
        newNode = Node(l[j])
        current_node.child[l[j]] = newNode
        current_node.child = dict(sorted(current_node.child.items()))
        current_node = newNode
        
   
            
tree.head.DFS(tree.head) 