import cv2

import matplotlib.pyplot as plt  # plt 用于显示图片
import matplotlib.image as mpimg  # mpimg 用于读取图片
import numpy as np

pic = mpimg.imread('cover.jpg')  # 读取和代码处于同一目录下的 lena.png
# 此时 lena 就已经是一个 np.array 了，可以对它进行任意处理
pic.shape  # (512, 512, 3)
pic=np.array(pic)
pic=cv2.cvtColor(pic, cv2.COLOR_BGR2RGB)
(B,G,R) = cv2.split(pic)#提取R、G、B分量
# cv2.imshow("Red",R)
# cv2.imshow("Green",G)
# cv2.imshow("Blue",B)
print(pic)
print(R)
print(R.shape)
# cv2.waitKey(0)

plt.show()

