def solution(a, b):
    s1 = int(str(a) + str(b))
    s2 = int(str(b) + str(a))
    if s1 >= s2:
        answer = s1
    else:
        answer = s2
    return answer