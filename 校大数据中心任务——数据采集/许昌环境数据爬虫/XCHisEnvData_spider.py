# encoding:utf8

from urllib import request
import pymysql
import json
import time
import execjs



def contentDownload(url):
    # xc_headers = {
    #     # "Accept": "* / *",
    #     # "Accept - Encoding":"gzip, deflate, sdch",
    #     # "Accept-Language": "zh-CN,zh;q=0.8",
    #     # "Connection": "keep-alive",
    #     # "Cookie":"onlyShowAirQualityInCityBoundingBox=101a115a108a97a102; cityName=24066a26124a35768",
    #     # "Host": "urbanair.msra.cn",
    #     # "Referer": "http://urbanair.msra.cn/",
    #     "User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2723.3 Safari/537.36",
    #     # "X-Requested-With":"XMLHttpRequest"
    # }
    req = request.Request(url)
    req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2723.3 Safari/537.36")
    res = request.urlopen(req)
    content = res.read().decode("utf8")
    print(content)
    return content

def dataWrite(data):
    conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='root', db='environment', charset='utf8')
    cursor = conn.cursor()
    try:
        insert_sql = "insert into xcenvironment values('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"%(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7])
        cursor.execute(insert_sql)
        conn.commit()
        print("%s   %s :数据成功存入数据库！" % (data[1], data[0]))
    except Exception as e:
        print(str(e))
        print("%s   %s :该数据在数据库中已存在！" % (data[1], data[0]))
    cursor.close()
    conn.close()




def countCircle(detaildata):

    for i in range(len(detaildata)):
        data = []
        if detaildata[i]["RegionID"] == "220":
            region = "许昌"
            data.append(region)
        else:
            continue
        Date = detaildata[i]["Date"]
        ctx = execjs.compile("""
            function changeDateFormate(cellval){
                var date = new Date(parseInt(cellval.replace("/Date(", "").replace(")/", ""), 10));
                var month = date.getMonth() + 1 < 10 ? "0" + (date.getMonth()+1) : date.getMonth() +1;
                var currentDate = date.getDate < 10 ? "0" + date.getDate() : date.getDate();
                return date.getFullYear() + "-" + month + "-" +currentDate;
        }
        """)
        data.append(ctx.call("changeDateFormate", Date))
        PM25 = detaildata[i]["AVG_PM25"]
        data.append(PM25)
        PM10 = detaildata[i]["AVG_PM10"]
        data.append(PM10)
        NO2 = detaildata[i]["AVG_NO2"]
        data.append(NO2)
        CO = detaildata[i]["AVG_CO"]
        data.append(CO)
        O3 = detaildata[i]["AVG_O3"]
        data.append(O3)
        SO2 = detaildata[i]["AVG_SO2"]
        data.append(SO2)
        print("--------data-----------")
        print(data)
        dataWrite(data)



def contentParser(content):
    json_cont = json.loads(content)
    if "DetailData" in json_cont.keys():
        detaildata = json_cont['DetailData']
        print("-------------------")
        print(detaildata)
        countCircle(detaildata)

def getEnvironmentData():
    try:
        url = "http://urbanair.msra.cn/U_Air/GetAirQuality?CityId=220&_=1514516984582"
        content = contentDownload(url)
        contentParser(content)
    except Exception as e:
        print("出项异常！一分钟后重试……")
        print("Exception: "+str(e))
        time.sleep(60)
        getEnvironmentData()

print("开始工作！")
getEnvironmentData()
print("结束工作！")
print("\n")