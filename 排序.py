x=int(input("x="))
y=int(input("y="))
z=int(input("z="))
list1=[x,y,z]
for i in range(len(list1)-1):
    for j in range(0,len(list1)-i-1):
        if list1[j]>list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j]
for p in list1:
    print(p)

