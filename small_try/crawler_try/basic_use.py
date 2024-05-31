#! python3
# coding: utf-8

from bs4 import BeautifulSoup
from lxml import etree
import requests
import chardet

def main():
    # 首次爬取
    url = "http://tipdm.com/"
    rq = requests.get(url)
    print(rq)
    print(rq.headers)
    print(rq.status_code)
    # print(rq.text)   # 这里就是返回网页的html

    # 完善http请求
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    response = requests.get(url, headers=headers, timeout=2)  # 发起请求
    response.encoding = chardet.detect(response.content)  # 设置响应内容的编码
    print(response)

    # xpath 使用
    with open("./data/html_doc.html") as f:
        html_doc = f.read()
    dom = etree.HTML(html_doc)

    print(dom.xpath("/html/head/title/text()"))  # 按html的dom树结构绝对路径拿数据
    print(dom.xpath('//body/p/a[1]/text()'))  # 加入了顺序（序号）用以精确指定目标元素
    print(dom.xpath('//body/p/a[@id="link2"]/text()'))  # 加入属性值，用以精确指定目标元素
    print(dom.xpath(".."))
    dom.xpath('//body/p/a[@id="link1"]/@href')  # 提取目标元素的属性值
    dom.xpath('//body/p/a[@id="link1"]/@class')  # 提取目标元素的属性值

    # BeautifulSoup 使用
    soup = BeautifulSoup(html_doc, 'lxml')    # 解析网页数据，得到BeautifulSoup对象
    # # 通过标签名获取元素
    # soup.title
    # soup.p
    # soup.a

    print(soup.select('html > head > title'))        # 绝对路径写法
    soup.select('body a')                     # 相对路径写法
    soup.select('p > a:nth-child(1)')         # 在路径中添加元素序号信息
    soup.select('p > a[id="link1"]')          # 在路径中添加元素属性信息


if __name__ == '__main__':
    main()
