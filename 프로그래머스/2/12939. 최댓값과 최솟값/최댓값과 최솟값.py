def solution(s):
    answer = list(map(int, s.split()))

    max1 = max(answer)
    min1 = min(answer)
    
    return f"{min1} {max1}"