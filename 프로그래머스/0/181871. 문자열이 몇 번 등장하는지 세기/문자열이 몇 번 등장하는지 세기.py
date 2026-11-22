def solution(myString, pat):
    answer = 0
    tmp = myString
    i = 0
    while tmp.find(pat) != -1:
        answer += 1
        tmp = tmp[tmp.find(pat)+1:]
    return answer