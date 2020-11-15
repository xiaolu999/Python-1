import requests                     #导入requests库
from bs4 import BeautifulSoup           #从bs4库中导入BeautifulSoup类
import re                               #导入re模块
import json                         #导入json库
#定义函数，根据填写的url参数获取数据
def getKeywordResult(keyword):
    url = 'http://www.baidu.com/s?wd='+keyword
    #异常处理
    try:
        r = requests.get(url, timeout=30)   #使用get函数打开指定的url
        r.raise_for_status()                #如果状态不是200，则引发异常
        r.encoding = 'utf-8'                #更改编码方式
        return r.text                   #返回页面内容
    except:
        return ""                       #发生异常返回空字符
#定义数据解析函数，用于找到符合条件的数据并返回
def parserLinks(html):
    soup = BeautifulSoup(html, "html.parser")   #将html对象转化为BeautifulSoup对象
    links = []                          #定义列表用于存储数据
    #找到所有符合条件的信息并遍历
    for div in soup.find_all('div', {'data-tools': re.compile('title')}):
        data = div.attrs['data-tools']      #获得属性值
        d = json.loads(data)                #将属性值转换成字典
        links.append(d['title'])            #返回数据加到列表之后
    return links                        #返回列表数据
#定义main函数用于调用函数及将得到的数据写入到文件
def main():
    html = getKeywordResult('Python程序设计教程') #调用获取页面内容函数
    ls = parserLinks(html)              #调用解析数据函数
    count = 1
    with open('121.txt','w', encoding = 'utf-8') as fd:            #将数据写入到12-4.txt文件中
        for i in ls:
            fd.write('[')
            fd.write(str(count))
            fd.write(']')
            fd.write(i)             #写入文件
            fd.write('\n')
            count += 1
    print('写入文件成功！')
main()                              #调用main函数
