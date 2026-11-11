def solution(common):
    a1, a2, a3 = common[0], common[1], common[2]
    if a3 - a2 == a2 - a1:
        d = a2 - a1
        return a1 + d * len(common)
    else:
        r = a2 / a1
        return a1 * (r ** len(common))