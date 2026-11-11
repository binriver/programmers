def solution(babbling):
    test = ["aya", "ye", "woo", "ma"]
    answer = 0
    for i in range(len(babbling)):
        for t in test:
            babbling[i] = babbling[i].replace(t, " ")
        if babbling[i].count(" ") == len(babbling[i]):
            answer += 1
    return answer