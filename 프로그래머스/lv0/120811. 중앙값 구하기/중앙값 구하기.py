def solution(array):
    a = len(array)
    b =(a // 2)
    array.sort()
    print(array)
    print(b)
    answer = array[b]
    return answer