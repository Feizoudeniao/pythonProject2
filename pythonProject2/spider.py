# http://www.51testing.com/html/04/category-catid-104.html
# 爬虫练习
from lxml import etree

import requests

# 发送请求并获取响应
url='http://www.51testing.com/html/04/category-catid-104-page-2.html'
response=requests.get(url)
# print(response)


# 获取页面编码格式
code=response.apparent_encoding
# print(code)
# 设置页面编码格式
response.encoding='GB18030'
content=response.text
# print(content)

# 将网页转换为dom格式
doc=etree.HTML(content)
# print(doc)

# 使用xpath获取网页信息
file=open('spider1.txt','w')
for i in range(1,11):
    a=doc.xpath(f'/html/body/div[6]/div[1]/div[{i}]/p/text()')[0]
    a1=''.join(a.split())
    print("第",i,"条：",a1)
    file.write("第"+str(i)+"条："+a1+"\n")