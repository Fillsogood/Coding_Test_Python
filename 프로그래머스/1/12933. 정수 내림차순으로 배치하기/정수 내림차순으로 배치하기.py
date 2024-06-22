def solution(n):
    answer = ""
    N = []
    for i in str(n):
        N.append(int(i))
    N = sorted(N, reverse=True)
    for j in N:
        answer += str(j)
    return int(answer)