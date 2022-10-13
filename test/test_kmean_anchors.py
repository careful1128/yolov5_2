from utils.autoanchor import kmean_anchors

if __name__ == '__main__':
    import os
    os.chdir('..')  #切换当前路径为上一个文件夹
    print(os.getcwd())
    a = kmean_anchors(dataset='./data/coco128.yaml')
    print(a)