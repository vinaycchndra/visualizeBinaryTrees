from collections import deque
class Tree:
    def __init__(self, val):
        self.val=val
        self.right = None
        self.left = None
        

def createBinaryTree(arr):
    
    if not len(arr):
        return None
    que = deque()
    root = Tree(arr[0])
    que.append(root)
    i = 1
    while que:
        node = que.popleft()
        if i<len(arr) and arr[i]:
            left = Tree(arr[i])
            que.append(left)
            node.left = left
        if i<len(arr):
            i += 1
        if i<len(arr) and arr[i]:
            right = Tree(arr[i])
            que.append(right)
            node.right = right
        if i<len(arr):
            i += 1
    return root
