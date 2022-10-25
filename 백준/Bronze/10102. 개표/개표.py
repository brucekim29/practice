num = int(input())
score = list(input())
if len(score) == num:
    if score.count('A') > score.count('B'):
        print('A')
    elif score.count('A') < score.count('B'):
        print('B')
    else:
        print('Tie')