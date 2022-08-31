import os
import cv2 as cv
from rembg.bg import remove

def getImagePath(root_dir):
    img_path_list = []

    for(root, dirs, files) in os.walk(root_dir):
        if len(files) > 0:
            for file_name in files:
                if os.path.splitext(file_name)[1] == ".jpg":
                    img_path = root + '/' + file_name
                    img_path = img_path.replace('\\', '/')
                    img_path_list.append(img_path)

    return img_path_list

def getTextPath(root_dir):
    txt_path_list = []

    for(root, dirs, files) in os.walk(root_dir):
        if len(files) > 0:
            for file_name in files:
                if os.path.splitext(file_name)[1] == ".txt":
                    txt_path = root + '/' + file_name
                    txt_path = txt_path.replace('\\', '/')
                    txt_path_list.append(txt_path)

    return txt_path_list

def removeBG(inputPath, outputPath):
    input = cv.imread(inputPath)
    output = remove(input)
    cv.imwrite(outputPath, output)

def img_trim(txtInputPath, imgInputPath, outputPath):
    img = cv.imread(imgInputPath)
    txt = open(txtInputPath, 'r')
    lines = txt.readlines()
    for index in range(len(lines)):
        line = lines[index].split(" ")
        x, y, w, h = int(line[1]), int(line[2]), int(line[3]), int(line[4])
        img = img[y:h, x:w]
        if index == 0: cv.imwrite(outputPath, img)
        else: cv.imwrite(outputPath + str(index), img)