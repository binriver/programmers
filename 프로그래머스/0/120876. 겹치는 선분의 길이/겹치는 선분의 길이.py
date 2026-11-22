def solution(lines):
    l1 = set(range(lines[0][0], lines[0][1]))
    l2 = set(range(lines[1][0], lines[1][1]))
    l3 = set(range(lines[2][0], lines[2][1]))
    
    result = (l1 & l2) | (l2 & l3) | (l3 & l1)
    return len(result)