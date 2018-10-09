# coding:utf8

import re
import urllib2
from bs4 import BeautifulSoup



def get_all_url():
    all_url = set()
    root_url = "http://quote.eastmoney.com/stocklist.html"
    response = urllib2.urlopen(root_url)
    if response.getcode() != 200:
        return None
    html_cont = response.read().decode('GBK').encode('utf8')
    if html_cont is None:
        return
    soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf8')
    nodes = soup.find_all('a', href=re.compile(r'http://quote.eastmoney.com/[s][z]\d+[\w]'))
    for node in nodes:
        node_text = node.get_text().decode('utf8')
        all_url.add('https://gupiao.baidu.com/stock/sz'+node_text[-7:-1]+'.html')
    length = len(all_url)
    return all_url, length
    

def url_manage():
    all_url, length = get_all_url()
    count = 1.0
    for url in all_url:
        try:
            html_cont = html_download(url)
            datas = html_parse(html_cont)
            if datas is None:
                continue
            data_output(datas)
            print ("当前进度  : {0:.2f}%".format(count/length*100))
            count = count + 1
        except:
            continue



def html_download(url):
    if url is None:
        return None
    #request = urllib2.Request()
    #request.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4033.400 QQBrowser/9.6.12624.400")
    response = urllib2.urlopen(url)
    if response.getcode() != 200:
        return None
    return response.read().decode("utf8").encode("utf8")
        


def html_parse(html_cont):
    if html_cont is None:
            return None
    soup = BeautifulSoup(html_cont, 'html.parser', from_encoding = 'utf8')
    name = soup.find('a', class_ = "bets-name").get_text().strip()
    datatime = soup.find('span', class_ ="state f-up").get_text().strip()
    price = soup.find('strong', class_ = '_close').get_text().strip()
    detail_node = soup.find('div', class_ = "bets-col-8")
    if detail_node is None:
        return
    detail_nodes = detail_node.find_all('dl')
    details = {}
    
    if name is None:
        details['name'] = 'null'
    else:
        details['name'] = name
   
    if datatime is None:
        details['dt'] = 'null'
    else: 
        details['dt'] = datatime
        
    if price is None:
        details['price'] = 'null'
    else:
        details['price'] = price
    for node in detail_nodes:
        text = node.find('dt').get_text().strip()
        data = node.find('dd').get_text().strip()
        if text == '最高':
            details['zg'] = data
        elif text == "最低":
            details['zd'] = data
        elif text == "今开":
            details['jk'] = data
        elif text == "昨收":
            details['zs'] = data
        elif text == "成交额":
            details['cje'] = data
        elif text == "成交量":
            details['cjl'] = data
        elif text == "净值":
            details['jz'] = data
        elif text == "折价率":
            details['zjlu'] = data
            
    return details
    #print details
    

def data_output(data):
    f = open('D://stock_info.txt', 'a')
    f.write("%s\t %s\t %s\t %s\t %s\t %s\t %s\t %s\t %s\t %s\t %s"
            %(data['name'], data['dt'], data['price'], data['zg'], data['zd'], data['jk'],
                data['zs'],data['cje'], data['cjl'], data['jz'], data['zjlu']))
    f.write("\n")
    f.close()   
    

    

url_manage()

