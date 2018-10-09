# encoding:utf8

from urllib import request
from bs4 import BeautifulSoup
import pymysql
import time



def htmlDownload(url):
    req = request.Request(url);
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2723.3 Safari/537.36')
    res = request.urlopen(req)
    html = res.read().decode("utf8").encode("utf8")
    return html


def htmlParser(html):
    soup = BeautifulSoup(html, 'html.parser', from_encoding="utf8")
    timenode = soup.find('div', class_ = 'remark')
    updatatime = timenode.get_text()[-15:]
    dataNode = soup.find("table")
    tr_node = dataNode.find_all("tr")
    data = []
    for i in range(1,5):
        d = []
        td_node = tr_node[i].find_all("td")
        for j in range(0,6):
            
            if j == 2:
                alt = td_node[j].find('img')['alt']
                d.append(alt[-4:])
            else:
                d.append(td_node[j].get_text())
        data.append(d)   
    return updatatime, data


def dataWriter(updatatime, data):
    connection = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='root', db='environment', charset='utf8')
    cursor = connection.cursor()
    
    for d in data:
        try:
            insert_sql = "insert into pdsenvironment(updatatime, AreaName, AQI, PollutionGrade, PM2_5, PM10, FirstItem) values('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (updatatime, d[0], d[1], d[2], d[3], d[4], d[5])
            cursor.execute(insert_sql)
            connection.commit() 
            print("%s   %s :数据已经存入数据库！"% (updatatime, d[0]))
        except Exception as e:
            print("%s   %s :该数据在数据库中已存在！"% (updatatime, d[0]))
    cursor.close()
    connection.close()
    

def getEnvironmentData():
    try:
        url = "http://www.86kongqi.com/city/pingdingshan.html"
        html = htmlDownload(url)
        updatatime, data = htmlParser(html)
        dataWriter(updatatime, data)
    except Exception as e:
        print("出现异常！一分钟后重试……")
        print("Exception: "+str(e))
        time.sleep(60)
        getEnvironmentData()
        

while True:
    print("开始工作!")
    getEnvironmentData();
    print("休息当中……")
    print("\n")
    time.sleep(3600)
