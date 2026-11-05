def solution(my_string):
    answer = []
    for C in range(65,91):
        answer.append(my_string.count(chr(C)))
    for c in range(97,123):
        answer.append(my_string.count(chr(c)))
    return answer