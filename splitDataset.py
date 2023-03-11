import os 
import random

trainval_percent = 0.9
train_percent = 0.9
txtfilepath = r"D:\Datasets\yolov8\data\labels"
txtsavepath = r"D:\Datasets\yolov8\data\ImageSets"
total_xml = os.listdir(txtfilepath)

num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

ftrainval = open(r'D:\Datasets\yolov8\data\ImageSets\trainval.txt', 'w')
ftest = open(r'D:\Datasets\yolov8\data\ImageSets\test.txt', 'w')
ftrain = open(r'D:\Datasets\yolov8\data\ImageSets\train.txt', 'w')
fval = open(r'D:\Datasets\yolov8\data\ImageSets\val.txt', 'w')

for i in list:
    name = total_xml[i][:9]
    if i in trainval:
        ftrainval.write('D:\Datasets\yolov8\data\images'+'\\'+name+'.jpg'+'\n')
        if i in train:
            ftrain.write('D:\Datasets\yolov8\data\images'+'\\'+name+'.jpg'+'\n')
        else:
            fval.write('D:\Datasets\yolov8\data\images'+'\\'+name+'.jpg'+'\n')
    else:
        ftest.write('D:\Datasets\yolov8\data\images'+'\\'+name+'.jpg'+'\n')

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()
