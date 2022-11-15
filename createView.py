from  BinaryTree  import  createBinaryTree
from collections import deque
arr = [1,2,3,5,6,4,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
#arr = [1,2,None,None,3,4]
root, level = createBinaryTree(arr)
que = deque([(root,0)])
arr_size = 2**level+1
i = 2

while que:
    c_1 =  arr_size//i                                                      # position in arr: c1+ind*c1*2  
    arr=[' ']*arr_size
    print("".join(arr))
    print("".join(arr))
    for _ in range(len(que)):
        node, ind = que.popleft()
        pos = c_1+c_1*ind*2
        arr[pos] = str(node.val)
        if node.left:
            que.append((node.left, ind*2))
        if node.right:
            que.append((node.right, ind*2+1))
    i *= 2
    print("".join(arr))

