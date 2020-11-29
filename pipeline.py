import redis
import time      #返回当前时间的时间戳
import threading #多线程
r=redis.Redis(host='127.0.0.1',port=6379,db=0)
# with open("D:/Update/result/总库0.txt", "r", encoding = 'UTF-8') as f:
#     for line in f:
#         r.sadd('总库0', line)

#1.普通的插入redis set集合方法
# begin = time.time()
# with open("D:/Update/result/总库0.txt", "r", encoding = 'UTF-8') as f:
#     for line in f:
#         r.sadd('总库0', line)
# end = time.time()
# print('time is %d seconds ' % (end - begin))

#2.利用redis pipline 管道技术
begin = time.time()
def loop():
    pipeline = r.pipeline()
    with open("D:/Update/result/总库0.txt", "r", encoding = 'UTF-8') as f:
        for line in f:
            r.sadd('总库0', line)
    pipeline.execute()
t = threading.Thread(target=loop,name="loopthread")
t.start()
t.join()
end = time.time()
print('time is %d seconds ' % (end - begin))
#
# #3.把需要插入的数据分块批量插入
# begin = time.time()
# for i in range(30):
#    ls = list(range(i*1000000,(i+1)*1000000))
#    r.sadd('xxxxx', *ls)
# end = time.time()
# print('time is %d seconds ' % (end - begin))