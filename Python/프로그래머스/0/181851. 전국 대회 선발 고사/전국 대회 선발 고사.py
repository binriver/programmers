def solution(rank, attendance):
    d = {}
    for idx, i in enumerate(rank):
        if attendance[idx] == True:
            d[idx] = i
    d_rank = sorted(d.items(), key = lambda x : x[1])
    a, b, c = d_rank[0][0], d_rank[1][0], d_rank[2][0]
    
    return 10000*a + 100*b + c