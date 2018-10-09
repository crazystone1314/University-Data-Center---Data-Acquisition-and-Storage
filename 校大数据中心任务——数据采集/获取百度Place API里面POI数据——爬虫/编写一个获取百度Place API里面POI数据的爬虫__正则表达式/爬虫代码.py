# encoding:utf8


import urllib2
import re



url = 'http://api.map.baidu.com/place/v2/search?query=ATM机&tag=银行page_size=1&page_num='
user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64)'
headers = {'User-Agent': user_agent}

file = open('test.txt', 'a')
pattern = re.compile(r'"name":"([\d\D]*?)",[\d\D]*?"lat":([\d\D]*?),[\d\D]*?"lng":([\d\D]*?)},')



for i in range(0, 20):
    try:
        url = url + str(i)+'&scope=1&region=北京&output=json&ak=ZkTi8FDVUUlAw3drrd5st2tduBSEq8kW'
        request = urllib2.Request(url, headers=headers);
        response = urllib2.urlopen(request)
        content = response.read().decode("utf-8")
        items = re.findall(pattern, content)
        for item in items:
            print ("name: "+ item[0])
            print ("lat: "+ item[1])  
            print ("lng: "+ item[2])
            print ("--------------")
            savestr = str(item[0]) + ',' +str(item[1]) + ',' +str(item[2]) +'\n'
            file.write(savestr)
               
    except urllib2.URLError, e:
        if hasattr(e, "code"):
            print e.code
        if hasattr(e, "reason"):
            print e.reason
            
file.close()   

