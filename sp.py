from re import *
import os
# code: UTF-8
# code: UTF-8
#str.decode(encoding='UTF-8',errors='strict')


#old为以列表，里面是装有要被替换的sub字符串，new是新字符串列表，dir是文件夹路径
def changelanguage( dir , old , new):
    if dir[-1].__ne__("\\"):
        dir += "\\"
    pathlst = os.listdir(dir)
    for filename in pathlst:
        if filename[-4:].__eq__(".jsp"):
            filename = (dir+filename).replace("\\", "/")
            lst=""
#必须先用“r”进行read
            with open(filename, "r", encoding="utf-8") as f:
                lst = f.read()
            lst = lst.replace(old, new)
            with open(filename, "w", encoding="utf-8") as f:
                f.write(lst)
    print("done!")

#dir是文件夹路径
def htmlTojsp(dir):
    if dir[-1].__ne__("\\"):
        dir += "\\"
    pathlst = os.listdir(dir)
    for filename in pathlst:
        if filename[-5:].__eq__(".html"):
            filename = (dir+filename).replace("\\", "/")
            words = ""
            filejsp = filename[:-5]+".jsp"
            with open(filename, "r", encoding="utf-8") as f:
                words = f.read()
            #此时words已经获得整个文件的文本
            words = '''<%@ page language="java" contentType="text/html; charset=utf-8"
    pageEncoding="utf-8"%>'''+"\n"+words
            print(words)
            with open(filejsp, "w+", encoding="utf-8") as f:
                f.write(words)
            os.remove(filename)
            if os._exists(filename) is False:
                print("done")




dir = r"C:\Users\14420\Desktop\网站html模板\test\Coco"
old = ["{session.username}"]
new = ["${sessionScope.username}"]
for i in range(len(old)):
    changelanguage(dir, old[i], new[i])




# old = "\"images/"
# new = "\"${pageContext.request.contextPath}/Coco/images/"
# changelanguage(dir,old,new)
# #htmlTojsp(dir)


# old = ["Dashboard", "UI Elements"]
# new = ["表格", "功能"]
#
# dir = r"C:\Users\14420\Desktop\网站html模板\test\Coco"
# for i in range(len(old)):
#     changelanguage(dir, old[i], new[i])





