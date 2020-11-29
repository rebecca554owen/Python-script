# -*- coding:utf-8 -*-
# 导入必要的模块
import pymysql  # MySQL数据库操作模块
import time  # 时间模块，用于性能统计

# 记录程序开始时间
begin = time.time()

# 打开数据库连接
# 参数说明：主机名，用户名，密码，数据库名，字符集
conn = pymysql.connect("localhost", "root", "qK6LjHDZ0KL4hZZC", "test", charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = conn.cursor()

# 如果表已存在则删除
cursor.execute("DROP TABLE IF EXISTS weibo")

# 创建数据表SQL语句
# 表结构：qq字段（11位，非空），phone字段（11位）
sql = "CREATE TABLE weibo ( qq varchar(11) NOT NULL, phone  varchar(11))"
cursor.execute(sql)

# 打开数据文件进行读取
with open("file.txt", 'r', encoding='UTF-8') as f:
    next(f)  # 跳过文件头
    # 逐行读取文件内容
    for line in f:
        # 使用"-"作为分隔符拆分每行数据
        line = line.split("-")
        # 执行SQL插入语句，将qq和phone插入数据库
        # line[0]对应qq，line[4]对应phone
        cursor.execute(("insert into weibo(qq,phone) values(%s,%s)"), [line[0], line[4]])
        # 提交事务
        conn.commit()
    
    # 关闭游标
    cursor.close()
    # 关闭数据库连接
    conn.close()

# 记录程序结束时间
end = time.time()
# 输出程序运行总耗时，单位为秒
print("time is %d seconds " % (end - begin))
