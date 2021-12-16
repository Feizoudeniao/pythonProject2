# 使用面向过程封装爬虫代码
# 多个页面抓取
from lxml import etree

import requests


# 发送请求并获取响应
def get_page(url):
    # url = 'http://www.51testing.com/html/04/category-catid-104-page-2.html'
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
    tmp = ""
    # 将网页转换为dom格式
    doc = etree.HTML(content)
    # print(doc)
    listm = []
    for i in range(1, 11):
        a = doc.xpath(f'/html/body/div[6]/div[1]/div[{i}]/p/text()')[0]
        a1 = ''.join(a.split())
        tmp = tmp + "第" + str(i) + "条" + "\t" + a1 + "\n"
    return tmp


# 使用xpath获取网页信息
def save_element(tmp,j):
    file = open('spider4.txt', 'a')
    file.write("第"+str(j)+"页"+tmp+"\n")
    file.close()


# url="http://www.51testing.com/html/04/category-catid-104.html"
# content = get_page(url)
# tmp = get_element(content)
# save_element(tmp)
if __name__ == '__main__':
    for j in range(1, 11):
        if j == 1:
            url = 'http://www.51testing.com/html/04/category-catid-104.html'
        else:
            url = f'http://www.51testing.com/html/04/category-catid-104-page-{j}.html'
        content = get_page(url)
        tmp = get_element(content)
        save_element(tmp,j)
