# -*- coding:utf-8 -*-
import redis  # redis数据库
import time  # 返回当前时间的时间戳

r = redis.Redis(host="127.0.0.1", port=6379, db=0)

# 1.普通的插入redis set集合方法
# begin = time.time()
# with open("D:/Update/result.txt", 'r', encoding='UTF-8') as f:
#     for line in f:
#         r.sadd("总库0", line)
# end = time.time()
# print("time is %d seconds " % (end - begin))

# 2.利用redis pipline 管道技术
begin = time.time()
pipeline = r.pipeline()
for i in range(1, 1 * 10 ** 6 + 1):  # 100W数据测试
    pipeline.sadd('方法2', i)
# with open("D:/Update/result.txt", 'r', encoding='UTF-8') as f:
#     for line in f:
#         pipeline.sadd("总库1", line)
pipeline.execute()
end = time.time()
print("time is %d seconds " % (end - begin))

# 3.把需要插入的数据分块批量插入
begin = time.time()
for i in range(10):
    ls = list(range(i * 100000, (i + 1) * 100000))  # 100W数据测试
    r.sadd('方法3', *ls)
end = time.time()
print('time is %d seconds ' % (end - begin))
