# encoding:utf8

import requests
import math
import json



def Count_Circle(count, data_details, f):
    for j in range(count):
        name = data_details['results'][j]['name'].decode('utf8')
        lat = data_details['results'][j]['location']['lat']
        lng = data_details['results'][j]['location']['lng']
        address = data_details['results'][j]['address'].decode('utf8')
        if 'telephone' in data_details['results'][j].keys():
            telephone = data_details['results'][j]['telephone'].decode('utf8')
        else:
            telephone = 'null'
        print("------------------------\n")
        print('%s\n %s\n %s\n %s\n %s\n'%(name, lat, lng, address, telephone))  
        f.write('%s, %s, %s, %s, %s\n'%(name, lat, lng, address, telephone))


def Num_Circle(num):
    f = open('result.txt', 'a')
    f.write('name, lat, lng, address\n')
    for i in range(num):
        url_details = 'http://api.map.baidu.com/place/v2/search?query=河南城建学院&tag=美食&page_size=10&page_num='+str(i)+'&location=33.777,113.197&radius=10000&output=json&ak=SjYD4LhAwtgpzE3PxowhN2MpFqnZ1BvN'
        data_details = json.loads(requests.get(url_details).content, encoding='utf8')
        if 'results' in data_details.keys():
            count = len(data_details['results'])
            Count_Circle(count, data_details, f)
        else:
            print("该页面results不存在！")
    
    f.close()
    print '数据采集完成！'





url = 'http://api.map.baidu.com/place/v2/search?query=河南城建学院&tag=美食&page_size=10&page_num=10&location=33.777,113.197&radius=10000&output=json&ak=SjYD4LhAwtgpzE3PxowhN2MpFqnZ1BvN'
data = json.loads(requests.get(url).content, encoding='utf8')
if 'total' in data.keys():
    print(data['total'])
    num = int(math.ceil(data['total']/10))
    Num_Circle(num)
else:
    print('total属性不存在！\n数据请求失败!\n')




    