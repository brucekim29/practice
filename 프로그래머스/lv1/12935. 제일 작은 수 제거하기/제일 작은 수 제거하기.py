def solution(arr):
    if len(arr) != 1:
        min_num = min(arr)
        index = arr.index(min_num)
        del(arr[index])
    else:
        arr = [-1]
    answer = arr
    return answer