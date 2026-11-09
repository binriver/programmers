def solution(strArr):
    answer = []
    for w in strArr:
        if "ad" not in w:
            answer.append(w)
    return answer