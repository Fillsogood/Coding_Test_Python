def solution(d, budget):
    answer = 0
    count = 0
    a = sorted(d)
    for i in a:
        answer+=i
        if answer <=budget:
            count +=1
            print(count)
    return count