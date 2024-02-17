def solution(d, budget):
    answer = 0
    count = 0
    sortD = sorted(d)
    for i in sortD:
        answer+=i
        if answer <= budget:
            count+=1
    return count