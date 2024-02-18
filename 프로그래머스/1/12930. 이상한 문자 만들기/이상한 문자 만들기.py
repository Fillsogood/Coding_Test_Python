def solution(s):
    answer = ''
    s=s.split(" ")
    
    for i in s:
        for j in range(len(i)):
            if j % 2 != 1:
                answer+=i[j].upper()
            elif j % 2 == 1:
                answer+=i[j].lower()
        answer += " "
    answer = answer[:-1]
    return answer