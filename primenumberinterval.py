lower_num =5
upper_num =100

for i in range(lower_num, upper_num+1):
    if i >1:
        for j in range(2, i):
            if (i % j)==0:
                break
        else:
            print(i)