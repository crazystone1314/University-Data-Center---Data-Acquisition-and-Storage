# -*- coding:utf-8 -*-


import os
import pandas as pd
# import sys

# reload(sys)
# sys.setdefaultencoding("utf8")
import pymysql

host = 'localhost'
username = 'root'
password = 'root'
db_name = 'workdb'
port = 3306
tablename = "test2012"

base_root = "d://Test/20012"  # 文件夹路径


# 获取所有文件路径
def get_filepath(base_root):
    filePaths = []
    for root, dirs, files in os.walk(base_root):
        for name in files:
            filePath = base_root + "/" + name
            filePaths.append(filePath)
    get_all_file_content(filePaths)


# 读取并规整文件内容
def read_file_content(filepath):
    df = pd.ExcelFile(filepath)
    content = df.parse("Sheet1")
    columns = range(8)
    content.columns = columns
    select = [1, 2, 3, 4, 5, 6, 7]
    content = pd.DataFrame(content, columns=select)
    content = content[content[3].notnull()]
    write_to_mysql(content)


# file_path = "d://Test/testaa.xls"
# c = read_file_content(file_path)
# c

# 获取文件所有内容
def get_all_file_content(filePaths):
    for filepath in filePaths:
        read_file_content(filepath)


# 将数据存入到数据库中

def write_to_mysql(content):
    connection = pymysql.connect(host=host, port=3306, user=username, passwd=password, charset='utf8', db=db_name)
    content.to_sql(name=tablename, con=connection, flavor="mysql", if_exists="append")
    connection.close()


get_filepath(base_root)
