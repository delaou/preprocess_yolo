import os

img_path = r"D:\Datasets\yolov8\data\images"
txt_path = r"D:\Datasets\yolov8\data\labels"

for txt_dir in os.listdir(txt_path):
    i = 0
    for img_dir in os.listdir(img_path):
        if txt_dir[:9] == img_dir[:9]:
            i = 1
            break
        else:
            pass
    if i == 1:
        pass
    else:
        os.remove(txt_path+'\\'+txt_dir)