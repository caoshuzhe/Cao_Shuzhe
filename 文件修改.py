# 读取test.txt内容，在开头和结尾追加"python"
with open("test.txt", "r") as f:
    content = f.read()

modified_content = "python" + content + "python"

with open("test_modified.txt", "w") as f:
    f.write(modified_content)

print("文件修改完成，新文件为test_modified.txt")
