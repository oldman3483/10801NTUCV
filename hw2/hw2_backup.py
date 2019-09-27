import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def binarylize(src):

    img = cv.imread(src, 0)
    row, col = img.shape

    for i in range(row):
        for j in range(col):
            if(img[i, j] < 128):
                img[i, j] = 0
            else:
                img[i, j] = 255

    return img

def drawHis(src):
    img = cv.imread(src, 0)
    row, col = img.shape
    his_list = np.zeros([256], dtype=int)

    for i in range(row):
        for j in range(col):
            px_value = img[i, j]
            his_list[px_value]+=1

    x = np.linspace(0, 255, 256)

    plt.figure()
    plt.xlabel("Pixel Value")
    plt.ylabel("Number")
    plt.title("Number of Pixel Value Figure")
    plt.plot(x, his_list)
    plt.xlim([0, 255])
    plt.show()
    plt.plot()
    
def check_4conn(src, row, col, top_down):
    label = 0
    if top_down:
        if src[row, col-1] != 0 :
            label = src[row, col-1]
        if (src[row-1, col] != 0) and (src[row-1, col] < label):
            label = src[row-1, col]
            
    return label 
    
def connect_component(src):
    binary = binarylize(src)
    label_rec = binary.copy
    row, col = label_rec.shape
    put_component = np.zeros([row, col], dtype=int)
    
    first, label = 1
   
    #first is top-down
    for i in range(row):
        for j in range(col):
            if binary[i, j] >0:
                if first:
                    binary[i, j] = label
                    first = 0
                    label+=1
                else:
                    give_label = check_4conn(binary, i, j, 1)
                    if give_label:
                        binary[i, j] = give_label
                    else:
                        binary[i,j] = label
                        label+=1
            put_component[i,j] = 255
    
    #second is bottom-up
    for i in range():
        for j in 
                        
                        



if __name__ == "__main__":

    img = 'lena.bmp'

    binary_img = binarylize(img)
    #drawHis(img)
    
    cv.imshow('binarylize', binary_img)
    cv.waitKey(0)