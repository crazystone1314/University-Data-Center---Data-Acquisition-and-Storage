# coding:utf8


import urllib2
from bs4 import BeautifulSoup
import re



def data_output(detail_info):
    f = open("estate_market_info.txt", 'a')
    f.write("%s\t %s\t %s\t %s\t %s\t %s\t %s\t %s\t %s\t %s\t %s\t %s\t %s\t %s\t %s\t %s\t %s\t %s\t %s\t %s"
            %(detail_info['city'],  detail_info['building_name'], detail_info['price'], detail_info["wylx"], detail_info["xmqw"]
              , detail_info["xwts"], detail_info["jzlx"], detail_info["zxzk"], detail_info["xwdz"], detail_info["jtzk"]
              , detail_info["tzs"], detail_info["jfsj"], detail_info["kfs"], detail_info["rjl"], detail_info["wyf"]
              , detail_info["lhl"], detail_info["zjzmj"], detail_info["wygs"],  detail_info["ysxkz"], detail_info['else']))
    f.write('\n')
    f.close()
    
def html_parse(html_cont):
    soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf8')
    detail__nodes = soup.find('div', class_ = 'details_cont').find_all('li')
    detail_info = {}
    else_info = ""
    for node in detail__nodes:
        key = node.find('span', class_ = 'span_b_6')
        if key is None:
            continue
        key_text = key.get_text().strip()
        value_text = node.get_text().strip()
        if "物业类别" == key_text:
            detail_info["wylx"] = value_text[5:]
        elif "项目区位" == key_text:
            detail_info["xmqw"] = value_text[5:]
        elif "项目特色" == key_text:
            detail_info["xwts"] = value_text[5:]
        elif "建筑类型" == key_text:
            detail_info["jzlx"] = value_text[5:]
        elif "装修状况" == key_text:
            detail_info["zxzk"] = value_text[5:]
        elif "项目地址" == key_text:
            detail_info["xwdz"] = value_text[5:] 
        elif "交通状况" == key_text:
            detail_info["jtzk"] = value_text[5:] 
        elif "投资商" == key_text:
            detail_info["tzs"] = value_text[4:]
        elif "交房时间" == key_text:
            detail_info["jfsj"] = value_text[5:]
        elif "开发商" == key_text:
            detail_info["kfs"] = value_text[4:]
        elif "容积率" == key_text:
            detail_info["rjl"] = value_text[4:]
        elif "物业费" == key_text:
            detail_info["wyf"] = value_text[4:]
        elif "绿化率" == key_text:
            detail_info["lhl"] = value_text[4:]
        elif "总建筑面积" == key_text:
            detail_info["zjzmj"] = value_text[6:]
        elif "物业公司" == key_text:
            detail_info["wygs"] = value_text[5:]
        elif "售楼地址" == key_text:
            detail_info["sldz"] = value_text[5:]
        elif "预售许可证" == key_text:
            detail_info["ysxkz"] = value_text[6:]
        else:
            else_info  = else_info + ", " + value_text
    detail_info['else'] = else_info
    return detail_info
            

def html_download(city, building_name, building_url, price):
    response = urllib2.urlopen(building_url)
    html_cont = response.read().decode("GBK").encode("utf8")
    detail_info = html_parse(html_cont)
    detail_info['city'] = city
    detail_info['building_name'] = building_name
    detail_info['price'] = price
    data_output(detail_info)
    
def url_manage():
    url = "http://www.hnloushi.com"
    response = urllib2.urlopen(url)
    html_cont = response.read().decode("GBK").encode("utf8")

    soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf8')
    data_node = soup.find('div', class_="mod3")

    citys = data_node.find_all('li', class_=re.compile(r'li1'))
    city_datas = []
    for city in citys:
        if city.get_text().strip() == '地市':
            continue
        city_datas.append(city.get_text().strip())

    building_names = data_node.find_all('li', class_="li2")
    building_name_datas = []
    building_url_datas = []
    for building_name in building_names:
        building_name_datas.append(building_name.get_text().strip())
        building_url = building_name.find('a')['href'].strip()
        if building_url == 'http://www.sjloushi.com/housetopic/sj_2016_gyl/':
            building_url_datas.append('http://www.sjloushi.com/newhousecenter/shownewhouse.asp?itemnum=9026') 
        else :
            building_url_datas.append(building_name.find('a')['href'].strip())


    prices = data_node.find_all('li', class_="li3")
    price_datas = []
    for price in prices:
        price_datas.append(price.get_text().strip())
 
    i = 0
    for building_url_data in building_url_datas:
        html_download(city_datas[i], building_name_datas[i], building_url_datas[i], price_datas[i])
 #       print city_datas[i], building_name_datas[i], building_url_data, price_datas[i]
        i = i + 1
        


def spider_main():
    url_manage()
    print "信息爬取完毕！"
    

    
spider_main()
    
