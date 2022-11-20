from collections import deque
class Tree:
    def __init__(self, val, level, pos):
        self.val=val
        self.level = level
        self.pos = pos
        self.right = None
        self.left = None
        self.image_coor = None
        

def createBinaryTree(arr):
    
    if not len(arr):
        return None
    que = deque()
    root = Tree(arr[0],1,0)   #initiating a root with 
    level_max = 1
    que.append(root)
    i = 1                     
    while que:
        node = que.popleft()
        level_max = max(node.level, level_max)
        if i<len(arr) and arr[i]!=None:
            left = Tree(arr[i], node.level+1,2*node.pos)
            que.append(left)
            node.left = left
    
        if i<len(arr):
            i += 1
        if i<len(arr) and arr[i]:
            right = Tree(arr[i], node.level+1,2*node.pos+1)
            que.append(right)
            node.right = right
        if i<len(arr):
            i += 1
    return root, level_max




## This script creates the binary trees from the level traversal list of the binary tree, the tree node has val-- value of the node, level -- the depth of the node in the binary tree, pos -- is the horizontal position of the node in a given level and left and right child of the node and coordinate of the node in the final image pan.
