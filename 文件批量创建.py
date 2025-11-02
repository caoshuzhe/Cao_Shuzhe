import os
import random
import string

# 新建test目录
os.makedirs("test", exist_ok=True)

# 用户指定文件数量和每行字符数
file_count = int(input("请输入要创建的文件数量："))
line_count = int(input("请输入每个文件的行数："))
char_per_line = int(input("请输入每行的字符数："))

# 生成随机可打印字符
def generate_random_str(length):
    return ''.join(random.choices(string.printable.strip(), k=length))  # 排除换行等控制字符

# 批量创建文件并写入内容
for i in range(file_count):
    filename = f"file_{i}.txt"
    with open(f"test/{filename}", "w") as f:
        for _ in range(line_count):
            f.write(generate_random_str(char_per_line) + '\n')

# 遍历test目录，修改文件名和文件内容
for filename in os.listdir("test"):
    # 修改文件名：添加"-python"后缀
    new_filename = filename.replace(".txt", "-python.txt")
    os.rename(f"test/{filename}", f"test/{new_filename}")
    
    # 修改文件内容：每行末尾添加"-python"
    with open(f"test/{new_filename}", "r") as f:
        lines = f.readlines()
    modified_lines = [line.strip() + "-python\n" for line in lines]
    with open(f"test/{new_filename}", "w") as f:
        f.writelines(modified_lines)

print("文件批量创建与修改完成！")