def solution(a, b, c, d):
    s = [a, b, c, d]
    l = len(set(s))
    s_list = list(set(s))
    
    if l == 1:
        answer = 1111 * s_list[0]
    elif l == 2:
        p, q = s_list[0], s_list[1]
        if s.count(p) == 2 or s.count(q) == 2:
            if p > q:
                answer = (p+q)*(p-q)
            else:
                answer = (p+q)*(q-p)
        elif s.count(p) == 3:
            answer = (10 * p + q) ** 2
        else:
            answer = (10 * q + p) ** 2
    elif l == 3:
        p, q, r = s_list[0], s_list[1], s_list[2]
        if s.count(p) == 2:
            answer = q * r
        elif s.count(q) == 2:
            answer = p * r
        else:
            answer = p * q
    else:
        answer = min(s)
        
    return answer