# -*- coding:utf-8 -*-
# 导入多线程模块，用于并发执行任务
import threading  # 多线程
# 导入时间模块，用于记录程序运行时间
import time  # 返回当前时间的时间戳

# 记录程序开始执行的时间
begin = time.time()

# 定义搜索函数
def loop():
    """
    文件搜索的核心函数，负责读取文件并查找目标字符串
    """
    # 打开目标文件，使用UTF-8编码读取
    with open("D:\\Update\\file.txt", 'r', encoding='UTF-8') as f:
        # 逐行读取文件内容
        for line in f:
            # 判断当前行是否包含目标QQ号码"836120472"
            if "836120472" in line:
                # 如果包含目标字符串，则打印该行内容
                print(line)

# 创建线程对象，指定目标函数和线程名称
t = threading.Thread(target=loop, name='loopthread')
# 启动线程
t.start()
# 等待线程执行完成
t.join()

# 记录程序结束时间
end = time.time()
# 输出程序运行总耗时，单位为秒
print("time is %d seconds " % (end - begin))
