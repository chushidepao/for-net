import requests
from bs4 import BeautifulSoup

# 获取532的节目列表

# 532的视频排序特点：如果是按照时间排序，则网页url为532movie.bnu.edu.cn/list/1/p/x.html, 其中x为第几页
#
#
#

# 获取532movie当前网页的总页码
def get_allpage_num(url):
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    source = r.content.decode(encoding=r.encoding)
    page_num = ""
    for i in source.split("&nbsp;"):
        if "当前:" in i:
            # print(i)
            page_num = i[5:-1]
            break
    return int(page_num)



# 获取532movie的网页列表
def get_movie_list():
    # url为532的html规则
    url = r"http://532movie.bnu.edu.cn/list/1/p/xxx.html"
    headpage_url = url.replace("xxx","1")
    # headpage 为替换页码
    request = requests.get(headpage_url)
    request.encoding = request.apparent_encoding
    all_page = get_allpage_num(headpage_url)
    lst=[]
    for i in range(all_page):
        new_url = url.replace("xxx", str(i+1))
        lst.append(new_url)
    for pageurl in lst:
        # 连接每个url
        page_reuqest = requests.get(pageurl)
        if page_reuqest.status_code != 200:
            print("connect error")
        page_reuqest.encoding = page_reuqest.apparent_encoding
        page_content = page_reuqest.content.decode(encoding=page_reuqest.encoding)
        soup = BeautifulSoup(page_content, "lxml")
        # 返回的soup是页面源
        yield soup

num =0
for soup in get_movie_list():
    lst = soup.find_all(attrs={'class':"thumbnail"})
    for i in lst:
        print(i.get("data-content"))
        print("************")
# print(num)







