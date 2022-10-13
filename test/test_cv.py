import math
import random
import cv2
import numpy as np
from PIL import Image

if __name__ == '__main__':
    path = "../data/images/bus.jpg"

    img = cv2.imread(path)   #[H，W，C]  BGR
    h,w,_ =img.shape
    width,height = w,h

    # # Center  中心点偏移
    # C = np.eye(3)
    # C[0, 2] = -h / 8 # x translation (pixels)
    # C[1, 2] = -w / 8  # y translation (pixels)
    #
    # # Rotation and Scale  旋转之后融合
    # R = np.eye(3)
    # a = random.uniform(-10, 10)
    # # a += random.choice([-180, -90, 0, 90])  # add 90deg rotations to small rotations
    # s = random.uniform(1 - 0.5, 1 + 0.5)
    # # s = 2 ** random.uniform(-scale, scale)
    # R[:2] = cv2.getRotationMatrix2D(angle=a, center=(0, 0), scale=s)  #计算旋转中心  转换矩阵（仿射变换）

    # Shear  计算剪切的矩阵
    S = np.eye(3)
    shear = 10
    S[0, 1] = math.tan(random.uniform(-shear, shear) * math.pi / 180)  # x shear (deg)
    S[1, 0] = math.tan(random.uniform(-shear, shear) * math.pi / 180)  # y shear (deg)


    # M = C
    # M = R
    M = S
    # M = R @ C
    img1= cv2.warpAffine(img,M[:2],dsize=(width,height),borderValue=(114,114,114))
    img2= cv2.warpPerspective(img, M, dsize=(width, height), borderValue=(114, 114, 114))

    Image.fromarray(img[:,:,::-1]).show()
    Image.fromarray(img1[:, :, ::-1]).show()
    Image.fromarray(img2[:, :, ::-1]).show()