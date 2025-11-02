# 读取两个文件并对比每一行
with open("test.txt", "r") as f1, open("copy_test.txt", "r") as f2:
    lines1 = f1.readlines()
    lines2 = f2.readlines()

# 逐行对比，输出不同行的编号（从1开始）
for i, (line1, line2) in enumerate(zip(lines1, lines2), 1):
    if line1 != line2:
        print(f"第{i}行内容不同")

# 处理行数不一致的情况
if len(lines1) != len(lines2):
    print(f"文件行数不一致，{len(lines1)}行 vs {len(lines2)}行")