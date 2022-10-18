list=[]
for a in range(1 , 6):
    list.append(int(input()))
    sum_num = 0    
    for i in list:
        if i>40:
            sum_num+=i
        else:
            sum_num+=40
print(sum_num//5)