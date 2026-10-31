def solution(str1, str2):
    answer = ''
    c = 0
    for n in str1:
        answer += n
        answer += str2[c]
        c += 1
    return answer