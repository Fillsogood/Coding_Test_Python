def solution(s):
    answer = True
    s = s.lower()
    Po=0
    Yo=0
    for i in s:
        if i == 'p':
            Po+=1
        elif i=='y':
            Yo+=1
    if Po==Yo:
        return True
    elif Po!=Yo:
        return False
        
    return True