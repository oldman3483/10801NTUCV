import cv2 as cv
import numpy as np
import math


def Upside_down(src):
    lena = cv.imread(src, 0)
    res = lena.copy()
    row = np.shape(res)[0]
    col = np.shape(res)[1]

    for i in range(0, int(row/2), 1):
        for j in range(0, col, 1):
            tmp = res[i][j]
            res[i][j] = res[row-1 - i][j]
            res[row-1 - i][j] = tmp
    return res

def Right_side_left(src):
    res = cv.imread(src, 0)
    row = np.shape(res)[0]
    col = np.shape(res)[1]

    for i in range(row):
        for j in range(int(col / 2)):
            tmp = res[i][j]
            res[i][j] = res[i][col-1 - j]
            res[i][col-1 - j] = tmp
    return res

def Diagonal_mirrored(src):
    lena = cv.imread(src, 0)
    res = lena.copy()
    row = np.shape(res)[0]
    col = np.shape(res)[1]

    for i in range(row):
        for j in range(i, col,1):
            if i != j:
                tmp = res[i][j]
                res[i][j] = res[j][i]
                res[j][i] = tmp
    return res


def rotate(src, deg):
    img = cv.imread(src, 0)
    row, col = img.shape

    M_shift = np.float32([[1, 0, int(row / math.sqrt(2) - row / 2)], [0, 1, int(col / math.sqrt(2) - col / 2)]])
    shifted = cv.warpAffine(img, M_shift, (int(row * math.sqrt(2) + 1), int(col * math.sqrt(2) + 1)))
    tranM = cv.getRotationMatrix2D((int(row * math.sqrt(2) + 1) / 2, int(col * math.sqrt(2) + 1) / 2), deg, 1)
    res = cv.warpAffine(shifted, tranM, (int(row * math.sqrt(2) + 1), int(col * math.sqrt(2) + 1)))

    return res

def shrink(src):
    img = cv.imread(src, 0)
    row = np.shape(img)[0]
    col = np.shape(img)[1]
    res = cv.resize(img, (int(row / 2), int(col / 2)), interpolation=cv.INTER_CUBIC)
    return res

def binarylize(src):
    res = cv.imread(src, 0)
    row, col = res.shape

    for i in range(row):
        for j in range(col):
            if res[i][j]>127:
                res[i][j] = 255
            else:
                res[i][j] = 0
    return res

if __name__ == "__main__":
    src = 'lena.bmp'
    Part1_a = Upside_down(src)
    Part1_b = Right_side_left(src)
    Part1_c = Diagonal_mirrored(src)

    Part2_d = rotate(src, -45)
    Part2_e = shrink(src)
    Part2_f = binarylize(src)

    cv.imshow('origin photo', cv.imread(src))
    cv.imshow('upside_down', Part1_a)
    cv.imshow('Right_side_left', Part1_b)
    cv.imshow('Diagonal Mirrored', Part1_c)
    cv.imshow('rotate 45 degree clockwise', Part2_d)
    cv.imshow('shrink', Part2_e)
    cv.imshow('binarylize', Part2_f)
    cv.waitKey(0)



