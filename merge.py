# -*- coding:utf-8 -*-
# 导入必要的模块
import os  # os模块中包含很多操作文件和目录的函数
import threading  # 多线程模块，用于并发执行任务
import time  # 时间模块，用于返回当前时间的时间戳

# 记录程序开始时间
begin = time.time()

# 定义要合并的文件所在目录路径
mergefiledir = "D:\\Update\\mergefiledir"  # 获取要合并的文件夹的路径

# 获取目录下所有文件名列表
filenames = os.listdir(mergefiledir)  # 获取合并文件夹中的文件名称列表

# 打开目标合并文件，以写入模式创建/打开，使用UTF-8编码
file = open("D:\\Update\\result.txt", 'w', encoding='utf8')  # 提前打开合并后的result.txt文件，如果不存在则创建

# 定义文件合并的主逻辑函数
def loop():
    """
    文件合并的核心函数，负责逐个读取文件并写入目标文件
    """
    for filename in filenames:  # 循环打开文件名称列表，向合并文件中逐行写入
        # 构造完整文件路径
        filepath = mergefiledir + '\\' + filename  # 文件路径=合并文件夹目录+转义符+文件名
        
        # 打开当前文件并逐行读取
        for line in open(filepath, 'r', encoding='utf8'):  # 遍历单个文件，读取行数
            file.writelines(line)  # 将当前行写入目标文件
        
        # 每个文件写入完成后添加换行符分隔
        file.write('\n')

# 创建并启动线程执行合并任务
t = threading.Thread(target=loop, name='loopthread')  # 创建线程对象，指定目标函数和线程名称
t.start()  # 启动线程
t.join()  # 等待线程执行完成

# 关闭目标文件
file.close()

# 记录程序结束时间
end = time.time()

# 输出程序运行总耗时，单位为秒
print("time is %d seconds " % (end - begin))
