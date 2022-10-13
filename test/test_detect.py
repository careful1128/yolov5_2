import torch


if __name__ == '__main__':
    #1.直接加载Github上训练好的模型
    #1.1 从Github上下载项目代码到本地路径（当前用户根目录下的路径）
    #1.2 从代码中调用hubconf.py文件进行模型的加载恢复
    # model = torch.hub.load('careful1128/yolov5_2', 'yolov5s')
    # model = torch.hub.load(r'C:\Users\lenovo\.cache\torch\hub\careful1128_yolov5_2_master','yolov5s',source='local')
    model = torch.hub.load(r'..', 'yolov5s', source='local')    #本地的图片和路径

    #Image路径
    img = "https://careful1128.com/images/zidane.jpg"    #or file,path,PIL,opencv,numpy,list
    img = "../data/images/bus.jpg"    #本地图片的检测
    img = "../data/images/zidane.jpg"
    #Inference推理预测
    results = model(img)

    #Results 结果展示
    results.print()   # or .show(), .save(), .crop(), .pandas(), etc.
    results.show()

    pass