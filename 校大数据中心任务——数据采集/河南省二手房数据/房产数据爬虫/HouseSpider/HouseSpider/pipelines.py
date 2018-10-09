# -*- coding: utf-8 -*-

import pymysql

class HousespiderPipeline(object):
    #对爬取的数据进行缺失值处理
    def process_item(self, item, spider):
        keys = item.keys()
        for key in keys:
            if item[key]:
                value = item[key]
                item[key] = value.strip()
            else:
                item[key] = "null"
        return item



class WriteToMysqlPipeline(object):

    host = "localhost"
    port = 3306
    username = "root"
    password = "root"
    db_name = "housedb"

    #将数据存储到数据库
    def process_item(self, item, spider):
        connect = pymysql.connect(host=self.host, port=self.port, user=self.username, passwd=self.password, charset='utf8', db=self.db_name)
        cursor = connect.cursor()
        sql_str = "insert into houseinfo(city, totalprice, housetype, conarea, unitprice, direction, floor, decoration, xiaoqu, region, architecturalage, islift, propertynature, residentialtype, buildingstructure, buildingtype, listingtime) " \
                  "values ('%s', '%s','%s', '%s','%s', '%s','%s', '%s', '%s', '%s', '%s','%s', '%s','%s', '%s','%s', '%s')" \
                  % (item['city'], item['totalprice'], item['housetype'], item['conarea'], item['unitprice'], item['direction'], item['floor'], item['decoration'], item['xiaoqu'], item['region'], item['architecturalage'], item['islift'], item['propertynature'], item['residentialtype'], item['buildingstructure'], item['buildingtype'], item['listingtime'])
        cursor.execute(sql_str)
        connect.commit()
        print '成功存入数据库！', item['city']
        cursor.close()
        connect.close()