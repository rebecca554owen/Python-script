# -*- coding:utf-8 -*-
# 导入redis模块，用于操作redis数据库
import redis  # redis数据库
# 导入时间模块，用于性能测试和计时
import time  # 返回当前时间的时间戳

# 创建redis连接对象，连接到本地redis服务器
r = redis.Redis(host="127.0.0.1", port=6379, db=0)

# 1.普通的插入redis set集合方法（已注释）
# 该方法逐条插入数据，效率较低
# begin = time.time()
# with open("D:/Update/result.txt", 'r', encoding='UTF-8') as f:
#     for line in f:
#         r.sadd("总库0", line)  # 逐条插入数据到redis集合
# end = time.time()
# print("time is %d seconds " % (end - begin))  # 输出耗时

# 2.利用redis pipline 管道技术
# 使用管道技术可以批量提交命令，减少网络往返时间
begin = time.time()  # 记录开始时间
pipeline = r.pipeline()  # 创建管道对象
# 插入100万条测试数据
for i in range(1, 1 * 10 ** 6 + 1):  # 100W数据测试
    pipeline.sadd('方法2', i)  # 将命令加入管道
# 文件插入示例（已注释）
# with open("D:/Update/result.txt", 'r', encoding='UTF-8') as f:
#     for line in f:
#         pipeline.sadd("总库1", line)
pipeline.execute()  # 批量执行管道中的所有命令
end = time.time()  # 记录结束时间
print("time is %d seconds " % (end - begin))  # 输出耗时

# 3.把需要插入的数据分块批量插入
# 将数据分块后批量插入，提高插入效率
begin = time.time()  # 记录开始时间
# 将100万数据分成10批，每批10万条
for i in range(10):
    # 生成当前批次的数据列表
    ls = list(range(i * 100000, (i + 1) * 100000))  # 100W数据测试
    # 使用*操作符将列表展开为多个参数
    r.sadd('方法3', *ls)  # 批量插入当前批次数据
end = time.time()  # 记录结束时间
print('time is %d seconds ' % (end - begin))  # 输出耗时
