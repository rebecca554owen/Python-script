# -*- coding:utf-8 -*-
import threading  # 多线程
import time  # 返回当前时间的时间戳

begin = time.time()


def loop():
    with open("D:\\Update\\file.txt", 'r', encoding='UTF-8') as f:
        for line in f:
            if "836120472" in line:
                print(line)


t = threading.Thread(target=loop, name='loopthread')
t.start()
t.join()
end = time.time()
print("time is %d seconds " % (end - begin))
