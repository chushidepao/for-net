from re import *
import os

def changelanguage( dir , old , new):
    if dir[-1].__ne__("\\"):
        dir += "\\"
    pathlst = os.listdir(dir)
    for filename in pathlst:
        if filename[-5:].__eq__(".html"):
            filename = (dir+filename).replace("\\", "/")
          #  print(filename)
          #  print(os._exists(filename))
            lst = open(filename).readlines()
           # print(lst)
            with open(filename, "w+")as f:
             #   print(lst)
                for i in lst:
                    f.write(i.replace(old, new))
    print("done!")


old = ["Dashboard", "UI Elements"]
new = ["表格", "功能"]
dir = r"C:\Users\14420\Desktop\网站html模板\test\Coco"
for i in range(len(old)):
    changelanguage(dir, old[i], new[i])





