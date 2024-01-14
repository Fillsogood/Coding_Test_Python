def solution(arr):
    answer = []
    temp = arr[0]
    answer.append(arr[0])
    for i in range(len(arr)):
        if temp != arr[i]:
            answer.append(arr[i])
            temp = arr[i]
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    return answer