from PIL import Image, ImageDraw, ImageFont
from  BinaryTree  import  createBinaryTree
from collections import deque
if __name__=="__main__":
    dx, dy = 80, 80
    arr = [3,5,1,6,2,0,8,None,None,7,4]
    root, level = createBinaryTree(arr)
    image_x = image_y = dx*(2**level+1)
    Dy = image_y//level
    new = Image.new(mode="RGBA", size=(image_x,image_y), color=(255,255,255,255))
    draw = ImageDraw.Draw(new)
    font = ImageFont.truetype("arial.ttf", dx//3)
    #draw.text((image_x//2+dx//2, image_y//2+dy//2), "2222", fill="black", anchor="mm", font=font)
    #new.show()





    #root, level = createBinaryTree(arr)
    que = deque([(root,0)])
    arr_size = 2**level+1
    i = 2
    coor_y = Dy//2
    
    while que:
        c_1 =  arr_size//i                                                      # position in arr: c1+ind*c1*2
        arr=[' ']*arr_size
        print("".join(arr))
        print("".join(arr))
        for _ in range(len(que)):
            node, ind = que.popleft()
            pos = c_1+c_1*ind*2
            coor_x = int(pos/arr_size*image_x)
            #draw.rectangle((coor_x,coor_y, coor_x+dx,coor_y+dy), outline=(0,0,115), width=dx//10)
            draw.arc([coor_x,coor_y, coor_x+dx,coor_y+dy], 0, 360, fill=(168,50,115), width=dx//10)       
            draw.text((coor_x+dx//2, coor_y+dy//2), str(node.val), fill="black", anchor="mm", font=font)
            arr[pos] = str(node.val)
            if node.left:
                que.append((node.left, ind*2))
            if node.right:
                que.append((node.right, ind*2+1))
        i *= 2
        coor_y += Dy
        print("".join(arr))

    new.show()
