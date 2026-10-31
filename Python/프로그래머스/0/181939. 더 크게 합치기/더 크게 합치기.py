def solution(a, b):
    s1 = int(f"{a}{b}")
    s2 = int(f"{b}{a}")
    if s1 >= s2:
        answer = s1
    else:
        answer = s2
    return answer