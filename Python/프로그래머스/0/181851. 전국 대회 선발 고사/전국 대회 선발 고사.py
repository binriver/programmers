def solution(rank, attendance):
    tmp = []
    for idx, i in enumerate(rank):
        if attendance[idx]:
            tmp.append((i, idx))
    tmp.sort()
    a, b, c = tmp[0][1], tmp[1][1], tmp[2][1]
    
    return 10000*a + 100*b + c