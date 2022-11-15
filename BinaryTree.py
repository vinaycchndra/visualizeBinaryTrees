from collections import deque
class Tree:
    def __init__(self, val, level):
        self.val=val
        self.level = level
        self.right = None
        self.left = None
        

def createBinaryTree(arr):
    
    if not len(arr):
        return None
    que = deque()
    root = Tree(arr[0],1)
    level_max = 1
    que.append(root)
    i = 1
    while que:
        node = que.popleft()
        level_max = max(node.level, level_max)
        if i<len(arr) and arr[i]:
            left = Tree(arr[i], node.level+1)
            que.append(left)
            node.left = left
    
        if i<len(arr):
            i += 1
        if i<len(arr) and arr[i]:
            right = Tree(arr[i], node.level+1)
            que.append(right)
            node.right = right
        if i<len(arr):
            i += 1
    return root, level_max
