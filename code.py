import cv2
import numpy as np
from matplotlib import pyplot as plt
import time

def lbp_pixel(img,x,y):
    center = img[x][y]
    num = []

    num.append(get_pixel(img,center,x-1,y-1))
    num.append(get_pixel(img,center,x-1,y))
    num.append(get_pixel(img,center,x-1,y+1))
    num.append(get_pixel(img,center,x,y+1))
    num.append(get_pixel(img,center,x+1,y+1))
    num.append(get_pixel(img,center,x+1,y))
    num.append(get_pixel(img,center,x+1,y-1))
    num.append(get_pixel(img,center,x,y-1))

    change = [1,2,4,8,16,32,64,128]

    num1 = 0

    for i in range(len(num)):
        num1 += num[i] * change[i]
    
    return num1

def get_pixel(img,center,x,y):
    num = 0
    try:
        if img[x][y] >= center:
              num = 1
    except:
        pass
    return num


start_time = time.time()

image = "C:\CN2\MAD101\code\LBP\Lena_grayscale.jpg"
image_2 = cv2.imread(image, 1)

a,b,c = image_2.shape

image_gray = cv2.cvtColor(image_2,
                        cv2.COLOR_BGR2GRAY)

image_lbp = np.zeros((a, b),
                   np.uint8)
   
for i in range(0, a):
    for j in range(0, b):
        image_lbp[i, j] = lbp_pixel(image_gray, i, j)   

end_time = time.time()

elapsed_time = end_time - start_time

print("elapsed_time: {0}".format(elapsed_time)+"[sec]")

#plt.imshow(image_2)
#plt.show()

   
plt.imshow(image_lbp, cmap ="gray")
plt.show()





