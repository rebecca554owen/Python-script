import time

begin = time.time()
buffersize = 2 ** 30  # 设置缓冲区，加速读取。
with open("D:/Update/file.txt") as f:
    while True:
        lines_buffer = f.readlines(buffersize)
        if not lines_buffer:
            break
        for line in lines_buffer:
            if "836120472" in line:
                print(line)
    end = time.time()
    print('time is %d seconds ' % (end - begin))
