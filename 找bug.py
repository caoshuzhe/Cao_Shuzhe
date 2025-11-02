#coding=utf-8
#错误在于列表长度因pop改变，索引会越界
#找bug
list=list(range(1000))
i=0
idx=0
while idx<len(list):
    if list[idx]%2==1:
        list.pop(idx)
    else:
        idx+=1
print(list)
