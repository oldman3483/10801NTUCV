import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv


def drawHis(img ,title):
    row = np.shape(img)[0]
    col = np.shape(img)[1]
    his_list = np.zeros([256], dtype=int)

    for i in range(row):
        for j in range(col):
            px_value = img[i, j]
            his_list[px_value]+=1

    x = np.linspace(0, 255, 256)

    plt.figure(1)
    plt.xlabel("Pixel Value")
    plt.ylabel("Number")
    plt.title(title)
    plt.plot(x, his_list)
    plt.xlim([0, 255])
    plt.show()
    plt.plot()


def divided_by_three(img):

    row = np.shape(img)[0]
    col = np.shape(img)[1]

    for i in range(row):
        for j in range(col):
            img[i, j] = img[i, j]/3

    return img

def his_equal(src):
    img = np.copy(src)
    row = np.shape(img)[0]
    col = np.shape(img)[1]

    px_times = np.empty([256])

    print(img)
    for r in range(row):
        for c in range(col):
            px_times[img[r, c]]+=1

    cdf = np.empty([256, 1])
    cdf[0, 0] = px_times[0]
    for num_times in range(0, 254, 1):
        cdf[num_times+1, 0] = px_times[num_times+1] + cdf[num_times, 0]

    cdfmin = cdf[0, 0]
    hv = np.zeros([256], dtype=np.float)
    for hv_value in range(255):
        hv[hv_value] = round((cdf[hv_value, 0]-cdfmin)/(row*col-cdfmin)*(255),0)

    for i in range(row):
        for j in range(col):
            img[i, j] = hv[img[i, j]]
    return img


if __name__ == "__main__":
    img = 'lena.bmp'
    img_mat = cv.imread(img)
    drawHis(img_mat, 'origin image')
    divid_by_3 = divided_by_three(img_mat)
    drawHis(divid_by_3, 'value divid by 3')
    window_name = "divided by 3"
    cv.imshow(window_name, divid_by_3)

    equal3 = his_equal(divid_by_3)
    drawHis(equal3, "equalization for divid 3")


    window_equal = "equal 3"
    print("is done")



    cv.imshow(window_equal, equal3)
    cv.waitKey(0)

