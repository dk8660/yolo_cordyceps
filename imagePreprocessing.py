from imgFunctions import img_trim, getImagePath, removeBG, getTextPath

root_dir = './runs/detect/cordyceps4'

img_path_list = getImagePath(root_dir)
txt_path_list = getTextPath(root_dir)

if len(img_path_list) != len(txt_path_list):
    print("이미지의 수와 좌표 값의 수가 같지 않습니다. img : txt = {} : {}".format(len(img_path_list), len(txt_path_list)))
    exit()

for i in range(len(img_path_list)):
    outputPath = img_path_list[i].replace("/cordyceps4", "/cordyceps4/trim")
    img_trim(txt_path_list[i], img_path_list[i], outputPath)
    print("{} image cut".format(i + 1))

trim_img_path_list = getImagePath(root_dir + "/trim")
count = 1
for path in trim_img_path_list:
    outputPath = path.replace("/trim", "/rembg")
    removeBG(path, outputPath)
    print("{} image background removed".format(count))
    count += 1