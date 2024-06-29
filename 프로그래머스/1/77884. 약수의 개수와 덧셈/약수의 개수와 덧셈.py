def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if count(i)%2 == 0:
            answer += i
        else:
            answer -= i
        
        
    print(answer)
            
        
    return answer

def count(n):
    a = 0
    for i in range(1,n+1):
        if n%i == 0:
            a += 1
    return a