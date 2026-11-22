def solution(numLog):
    answer = ""
    rule = {1:"w", -1:"s", 10:"d", -10:"a"}
    for i in range(len(numLog)-1):
        answer += rule[numLog[i+1] - numLog[i]]
    return answer