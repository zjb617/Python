from bs4 import BeautifulSoup
import requests


def getHTML(url):
    r = requests.get(url)
    return r.content


def parseHTML(html):
    soup = BeautifulSoup(html, "html.parser")

    body = soup.body
    company_middle = body.find("div", attrs={"id": "page-container"})
    tmp = company_middle.find(
        "div", attrs={"class": "container container-padding jc-layout"})
    company_list_ct = tmp.find("div", attrs={"class": "container-list"})

    # find_all获得该标签下所有html
    for company_ul in company_list_ct.find_all("ul", attrs={"class": "company-list"}):
        for company_li in company_ul.find_all("li"):
            company_url = company_li.a["href"]
            company_info = company_li.get_text()  # get_text获得标签里的文字
            print(company_info, company_url)

URL = "http://www.cninfo.com.cn/new/snapshot/companyListCn"
html = getHTML(URL)
parseHTML(html)
#由于反爬（动态异步传输，一些元素在源代码里不显示）