def solution(a, b):
    answer = 0
    result = map(lambda x, y: x * y, a, b)
    result = list(result)
    for i in result:
        answer += i
    
    return answer