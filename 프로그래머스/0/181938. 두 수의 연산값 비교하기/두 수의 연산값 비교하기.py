def solution(a, b):
    s1 = int(f"{a}{b}")
    s2 = 2 * a * b
    if s1 >= s2:
        answer = s1
    else:
        answer = s2
    return answer