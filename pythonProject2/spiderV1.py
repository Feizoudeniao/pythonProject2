# 使用面向过程封装爬虫代码
from lxml import etree

import requests


# 发送请求并获取响应
def get_page():
    url = 'http://www.51testing.com/html/04/category-catid-104-page-2.html'
    response = requests.get(url)
    # print(response)

    # 获取页面编码格式
    code = response.apparent_encoding
    # print(code)
    # 设置页面编码格式
    response.encoding = 'GB18030'
    content = response.text
    # print(content)
    return content


def get_element(content):
    tmp=""
    # 将网页转换为dom格式
    doc = etree.HTML(content)
    # print(doc)
    listm=[]
    for i in range(1, 11):
        a = doc.xpath(f'/html/body/div[6]/div[1]/div[{i}]/p/text()')[0]
        tmp=tmp+str(i)+a+"\n"
    return tmp


# 使用xpath获取网页信息
def save_element(tmp):
    file = open('spider2.txt', 'w')
    file.write(tmp)
    file.close()


content = get_page()
tmp = get_element(content)
save_element(tmp)
