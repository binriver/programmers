def solution(n, control):
    rule = {"w":1, "s":-1, "d":10, "a":-10}
    for c in control:
        n += rule[c]
    return n