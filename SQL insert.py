#!/usr/bin/python3
import pymysql
import time

begin = time.time()
# 打开数据库连接
conn = pymysql.connect("localhost", "root", "qK6LjHDZ0KL4hZZC", "test", charset='utf8')
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS weibo")
# 创建数据表SQL语句
sql = "CREATE TABLE weibo ( qq varchar(11) NOT NULL, phone  varchar(11))"
cursor.execute(sql)
# 使用 execute()  方法执行 SQL 查询
with open("C:/Users/SUYI/Desktop/file.txt", "r", encoding='UTF-8') as f:
    next(f)
    for line in f:
        line = line.split("-")
        # strip（）＃ 可以根据不同的分隔符分隔，将数据拆分两个元素
        cursor.execute(("insert into weibo(qq,phone) values(%s,%s)"), [line[0], line[4]])
        conn.commit()
    cursor.close()
    conn.close()
    end = time.time()
    print('time is %d seconds ' % (end - begin))
