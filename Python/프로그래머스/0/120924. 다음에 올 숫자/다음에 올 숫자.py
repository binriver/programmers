def solution(common):
    a0 ,a1, a2 = common[0:3]
    
    if a2 - a1 == a1 - a0:
        d = a1 - a0
        return common[-1] + d
    else:
        r = a1 // a0
        return common[-1] * r