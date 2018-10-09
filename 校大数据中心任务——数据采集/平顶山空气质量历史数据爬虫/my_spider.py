# encoding:utf8

from urllib import request
from bs4 import BeautifulSoup
import pymysql
import time



def htmlDownload(url):
    req = request.Request(url);
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2723.3 Safari/537.36')
    res = request.urlopen(req)
    html = res.read().decode("GBK").encode("utf8")
    return html


def htmlParser(html):
    soup = BeautifulSoup(html, 'html.parser', from_encoding="utf8")
    div_node = soup.find('div', class_ = 'box p')
    ul_Node = div_node.find("ul")
    tr_nodes = ul_Node.find_all("li")
    url_data = []
    for node in tr_nodes:
        a = node.find('a')
        url = 'http://www.tianqihoubao.com'+a['href']
        url_data.append(url)
    return url_data 


def dataWriter(data):
    connection = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='root', db='environment', charset='utf8')
    cursor = connection.cursor()
    
    for d in data:
        try:
            insert_sql = "insert into pdsenvironment_1(dt, quality_grade, AQI, AQI_rank, PM2_5, PM10, SO2, NO2, CO, O3) values('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (d[0], d[1], d[2], d[3], d[4], d[5], d[6], d[7], d[8], d[9])
            cursor.execute(insert_sql)
            connection.commit() 
            print("%s :数据已经存入数据库！"% (d[0]))
        except Exception as e:
            print("%s :该数据在数据库中已存在！"% (d[0]))
    cursor.close()
    connection.close()
    

def url_html_Parser(url):
    html = htmlDownload(url)
    soup = BeautifulSoup(html, 'html.parser', from_encoding="utf8")
    dataNode = soup.find("table")
    tr_node = dataNode.find_all("tr")
    data = []
    for i in range(1,len(tr_node)):
        d = []
        td_node = tr_node[i].find_all("td")
        for j in range(0,len(td_node)):
                text = td_node[j].get_text().strip()
                d.append(text)
        data.append(d)
    return data   

def getData(urls):
    for url in urls:
        try:
            data = url_html_Parser(url)
            dataWriter(data)
        except Exception as e:
            print("出现异常！十秒后重试……")
            print("Exception: "+str(e))
            time.sleep(10)
            getData(url)
    

def getEnvironmentData():
    try:
        url = "http://www.tianqihoubao.com/aqi/pingdingshan.html"
        html = htmlDownload(url)
        urls = htmlParser(html)
        getData(urls)
    except Exception as e:
        print("出现异常！一分钟后重试……")
        print("Exception: "+str(e))
        time.sleep(60)
        getEnvironmentData()
        


print("开始工作!")
getEnvironmentData();
print("工作完毕！")
print("\n")
