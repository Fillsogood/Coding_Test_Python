def solution(n):
    answer = [n]
    X=n
    while X>1:
        if X % 2==0:
            X=X/2
            answer.append(X)
        elif X%2==1:
            X=3*X+1
            answer.append(X)
            
    return answer