from PIL import Image, ImageDraw, ImageFont
from  BinaryTree  import  createBinaryTree
from collections import deque
import math
from input import arr

def coordinateLocator(x1,y1,x2,y2,dx, right):
    theta_1 = math.atan(abs(x2-x1)/abs(y2-y1))*180/math.pi
    theta_2 = 90-theta_1
    theta_1 = theta_1*math.pi/180
    theta_2 = theta_2*math.pi/180
    if right:
        x1,y1 = x1+dx*math.sin(theta_1), y1+dx*math.cos(theta_1)
        x2,y2 = x2-dx*math.cos(theta_2),y2-dx*math.sin(theta_2)
    else:
        x1,y1 = x1-dx*math.sin(theta_1), y1+dx*math.cos(theta_1)
        x2,y2 = x2+dx*math.cos(theta_2),y2-dx*math.sin(theta_2)
    return [(x1,y1),(x2,y2)]



if __name__=="__main__":
    dx, dy = 80, 80
    root, level = createBinaryTree(arr)
    image_x = image_y = dx*(2**level+1)
    Dy = image_y//level
    new = Image.new(mode="RGBA", size=(image_x,image_y), color=(255,255,255,255))
    draw = ImageDraw.Draw(new)
    font = ImageFont.truetype("arial.ttf", dx//3)

    
    # Below loop is for drawing individual node and its value into the image and storing the coordinates of the code into the Tree node itself, it uses iterative BFS

    que = deque([root])
    arr_size = 2**level+1
    i = 2
    coor_y = Dy//2 
    while que:
        c_1 =  arr_size//i                                                      # c1+node.pos*c1*2 is the actually x coordinate of the node which is linearly mapped to the image
        for _ in range(len(que)):
            node = que.popleft()
            pos = c_1+c_1*node.pos*2
            coor_x = int(pos/arr_size*image_x)
            draw.arc([coor_x,coor_y, coor_x+dx,coor_y+dy], 0, 360, fill=(168,50,115), width=dx//10)       
            draw.text((coor_x+dx//2, coor_y+dy//2), str(node.val), fill="black", anchor="mm", font=font)
            node.image_coor = (coor_x+dx//2, coor_y+dy//2)
            
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
        i *= 2
        coor_y += Dy
    

    # Below loop draws lines to the image between the nodes from their coordinates which were stored into the node.image_coor from the previous loop by using the iterative DFS
    stack = [root]
    while stack:
        node = stack.pop()
        x1,y1 = node.image_coor

        if node.left:
            x2,y2 = node.left.image_coor
            array = coordinateLocator(x1,y1,x2,y2,dx//2, False)
            draw.line(array, fill=(0,0,115),width=dx//40)
            stack.append(node.left)
        
        if node.right:
            x2,y2 = node.right.image_coor
            array = coordinateLocator(x1,y1,x2,y2,dx//2, True)
            draw.line(array, fill=(0,0,115),width=dx//40)
            stack.append(node.right)
        
    new.show()
