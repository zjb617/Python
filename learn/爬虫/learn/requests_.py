import requests
r1 = requests.get('http://cn.bing.com/search?q=requests')  # get方法
post_data = {
    'stock': '000001',
    'searchkey': '',
    'category': 'category_ndbg_szsh',
    'pageNum': '1',
    'pageSize': '',
    'column': 'szse_main',
    'tabName': 'fulltext',
    'sortName': '',
    'sortType': '',
    'limit': '',
    'seDate': ''
}

r2 = requests.post(
    'http://www.cninfo.com.cn/cninfo-new/announcement/query', data=post_data)  # post方法

print(r1.status_code)  # 状态码，正常是200
print(r1.encoding)  # 文件编码，比如utf-8
print(r1.content)  # 文件全文

print(r1.json)  # 把请求回来的json数据转成Python字典并返回

r3 = requests.get(
    'http://www.cninfo.com.cn/finalpage/2015-03-13/1200694563.PDF', stream=True)  # 请求
r3.raw.read(1)  # 读取文件（最好在括号里加一下个数，只读前面几个）


def getHTML(url):
    r = requests.get(url)
    return r.content


if __name__ == "__main__":
    url = 'https://zhuanlan.zhihu.com/xmucpp'
    html = getHTML(url)
    print(html)
