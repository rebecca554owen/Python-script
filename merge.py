# -*- coding:utf-8 -*-
import os        #os模块中包含很多操作文件和目录的函数
import threading #多线程
import time      #返回当前时间的时间戳

begin = time.time()
mergefiledir = os.getcwd()+ '\\mergefiledir' # 获取要合并的文件夹的路径
filenames = os.listdir(mergefiledir)         # 获取合并文件夹中的文件名称列表
file = open('result.txt', 'w', encoding='utf8')# 提前打开合并后的result.txt文件，如果不存在则创建
def loop():
    for filename in filenames:  # 循环打开文件名称列表，向合并文件中逐行写入
        filepath = mergefiledir + '\\' + filename #文件路径=合并文件夹目录+转义符+文件名
        # 遍历单个文件，读取行数
        for line in open(filepath,'r', encoding='utf8'):
            file.writelines(line)
        file.write('\n')
t = threading.Thread(target=loop,name="loopthread")
t.start()
t.join()
file.close()
end = time.time()
print('time is %d seconds ' % (end - begin))