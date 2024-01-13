def solution(s):
    a = ['zero','one','two','three','four','five','six','seven','eight','nine']
    b = ['0','1','2','3','4','5','6','7','8','9']
    
    for key , value in zip(a,b):
           s = s.replace(key,value)
    return int(s)
