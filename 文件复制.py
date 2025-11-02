import random
import string

# 生成随机ASCII非控制字符（可打印字符：32-126）
def generate_random_char():
    return chr(random.randint(32, 126))

# 用户指定行数
lines = int(input("请输入要生成的行数："))

# 创建并写入test.txt
with open("test.txt", "w") as f:
    for _ in range(lines):
        line = ''.join([generate_random_char() for _ in range(10)])  # 每行10个随机字符
        f.write(line + '\n')

# 复制文件到copy_test.txt
with open("test.txt", "r") as src, open("copy_test.txt", "w") as dst:
    dst.write(src.read())

print("文件复制完成！")