def solution(arr):
    answer = 0
    le = len(arr)
    for i in arr:
        answer += i
    answer = answer / le
    return answer