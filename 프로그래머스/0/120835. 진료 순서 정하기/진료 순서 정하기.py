def solution(emergency):
    answer = []
    for i in emergency:
        tmp = 1
        for j in emergency:
            if i < j:
                tmp += 1
        answer.append(tmp)
    return answer