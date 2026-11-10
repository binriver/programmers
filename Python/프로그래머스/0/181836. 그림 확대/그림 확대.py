def solution(picture, k):
    answer = []
    for p in picture:
        tmp = " ".join(p).split(" ")
        word_tmp = ""
        for t in tmp:
            word_tmp += t * k
        for i in range(k): 
            answer.append(word_tmp)
    return answer