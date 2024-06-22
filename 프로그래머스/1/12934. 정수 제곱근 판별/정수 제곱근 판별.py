def solution(n):
    answer = 0
    num = n** 0.5
    if int(num)*int(num) != n:
        return -1
    else:
        return int(num+1)*int(num+1)
    return answer