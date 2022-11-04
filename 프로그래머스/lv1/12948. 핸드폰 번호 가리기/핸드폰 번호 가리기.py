def solution(phone_number):
    front = len(phone_number[:-4]) * '*'
    answer = front + phone_number[-4:len(phone_number)]
    return answer