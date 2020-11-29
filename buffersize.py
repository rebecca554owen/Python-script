# -*- coding:utf-8 -*-
import time

# 记录程序开始时间
begin = time.time()

# 设置内存缓冲区大小，1024字节（1KB），用于加速大文件读取
buffersize = 2 ** 10  # 设置内存缓冲区，加速读取。

# 打开指定路径的文件，使用UTF-8编码读取
with open("D:\\Update\\file.txt", 'r', encoding='utf-8') as f:
    while True:
        # 按缓冲区大小读取文件内容
        lines_buffer = f.readlines(buffersize)
        
        # 如果读取内容为空，表示文件读取完毕，退出循环
        if not lines_buffer:
            break
            
        # 遍历缓冲区中的每一行内容
        for line in lines_buffer:
            # 判断当前行是否包含目标字符串"836120472"
            if "836120472" in line:
                # 如果包含目标字符串，则打印该行内容
                print(line)

# 记录程序结束时间
end = time.time()

# 输出程序运行总耗时，单位为秒
print("time is %d seconds " % (end - begin))
