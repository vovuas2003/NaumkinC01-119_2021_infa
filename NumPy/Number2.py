import cv2
import numpy as np
def func1d(a):
    return(a * weights)
img = cv2.imread("pick.jpg")
print(img.shape)
weights = np.array([0.299, 0.587, 0.114])
img2 = np.apply_along_axis(func1d, 2, img)
img2 = np.sum(img2, axis=2)
cv2.imwrite('grey_pick.jpg', img2)
