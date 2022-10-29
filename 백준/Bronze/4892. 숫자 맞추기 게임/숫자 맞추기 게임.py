count = 0
while True:
    n=int(input());n_1 = n*3;n_2 = n_1//2;n_3 = n_2*3;n_4 = n_3 // 9
    if n == 0:
        break
    elif n_1 % 2 == 0:
        count+=1
        n_1even = 'even'
        print("{}. {} {}".format(count,n_1even, n_4))
    else:
        count+=1
        n_1odd = 'odd'
        print("{}. {} {}".format(count,n_1odd, n_4))