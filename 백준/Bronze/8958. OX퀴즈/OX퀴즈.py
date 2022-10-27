t = int(input())
for n in range(t):
    result = input();total = 0;score=0
    for r in result:
        if r == 'O':
            if r == r:
                score +=1;total += score
        else:
            score = 0
    print(total)