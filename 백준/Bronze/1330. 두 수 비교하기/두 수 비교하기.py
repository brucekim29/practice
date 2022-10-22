a, b = map(int, input().split())

while True:
    if a > b:
        print('>')
        break
    elif a < b:
        print('<')
        break
    else:
        print('==')
        break