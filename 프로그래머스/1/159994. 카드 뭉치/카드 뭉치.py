def solution(cards1, cards2, goal):
    answer = []
    cards1_len = len(cards1)
    cards2_len = len(cards2)
    a=0
    b=0
    for word in goal:
        if a<cards1_len and word == cards1[a]:
            answer.append(cards1[a])
            a+=1
        if b<cards2_len and word == cards2[b]:
            answer.append(cards2[b])
            b+=1
    print(answer)
    if answer == goal:
        return "Yes"
    else:
        return "No"