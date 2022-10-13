import torch
import numpy as np

from utils.augmentations import letterbox

if __name__ == '__main__':
    im = np.random.rand(200 ,300 ,3 )

    im,a,b= letterbox(
        im,
        new_shape=(640, 640),
        color=(114,114,114),
        auto=True,   #  True表示仅将最大值设置为目标值，短边等比例缩放（满足是stride参数的倍数）+填充；False表示所有边缩放到目标值
        scaleFill=False,  # 当auto为False的时候，当前参数为True的时候生效，不做等比列缩放
        scaleup=True,  # 当设置为False的时候，表示图像小于目标尺寸，那么直接原始图像输出；大于的时候会做缩放
        stride=32
    )
    print(im.shape)
    print(a)
    print(b)


    # def letterbox(im, new_shape=(640, 640), color=(114, 114, 114), auto=True, scaleFill=False, scaleup=True, stride=32):