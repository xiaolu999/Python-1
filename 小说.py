
import urllib.request
from bs4 import BeautifulSoup
import os


# 下载目标小说的具体章节的内容并以文本形式存储到本地
def get_novalTxt(url):
    # 通过request的urlopen方法打开url
    resp = urllib.request.urlopen(url).read().decode('gbk')

    bs = BeautifulSoup(resp, 'html.parser')
    name = str(bs.find('title').string).split('_')[0]  # 获得小说名字

    if not os.path.exists(name):  # 如果存储小说的文件夹已经存在则不创建，否则创建存储小说的文件夹，名为小说名
        os.mkdir(name)

    title = bs.find('strong', class_='l jieqi_title').string
    title = str(title).replace('章节目录 ', '')  # 获得小说章节名字
    fileName = title + '.txt'
    print(title, '正在下载')

    # 把小说内容给切出来
    content = str(bs.find('div', class_='mainContenr'))
    content = content.replace('\xa0' * 8, '').replace('<br/>', '').replace(
        '<div class="mainContenr" id="content"><script type="text/javascript">style5();</script>', '').replace(
        '<script type="text/javascript">style6();</script></div>', 'txt')
    content = title + '\n\n' + content
    f = open(name + '/' + fileName, 'w', encoding='utf-8')  # 以只写的方式打开存储小说的文件夹
    f.writelines(content)
    print(title, '下载完成')


if __name__ == '__main__':
    # 目标小说的url，名字可以随便取，但建议url，易解读,下同理
    url = ''
    # 通过request的urlopen（）方法打开url,并用read（）方法读出内容,加上decode（）方法，将内容以gbk
    resp = urllib.request.urlopen(url).read().decode('gbk')
    bs = BeautifulSoup(resp, 'html.parser')

    # 先找到小说章节链接所在的div标签即class=’clearfix dirconone‘的div标签,
    # BeautifulSoup的find_all方法，此行代码即找到div标签，class为clearfix dirconone的所有标签
    txt = bs.div.find_all('div', class_='clearfix dirconone', )  # 由于class在python中是关键字，所以find_all方法使用class_来代表class，

    # 在找到上面找到的div标签的里面的a标签，获得其href的内容
    bs = BeautifulSoup(str(txt), 'html.parser')
    result = bs.find_all('a')

    for i in result:
        href = i.get('href')  # 获得‘a'标签里面的href的内容
        get_novalTxt(href)