def solution(picture, k):
    answer = []
    for i in range(len(picture)):
        tmp = picture[i].replace(".", "."*k).replace("x", "x"*k)
        for t in range(k): 
            answer.append(tmp)
    return answer