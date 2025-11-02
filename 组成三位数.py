count=0
for i in range(1,5,1):
    for j in range(1,5,1):
        if i!=j:
            for k in range(1,5,1):
                if k!=i and k!=j:
                    print(str(i)+str(j)+str(k))
                    count+=1
print(count)

