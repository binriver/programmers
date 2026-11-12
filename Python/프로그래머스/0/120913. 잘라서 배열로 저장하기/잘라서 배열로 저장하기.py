def solution(my_str, n):
    answer = []
    i, j = 0, n
    if len(my_str) % n == 0:
        for i in range(0, len(my_str), n):
            answer.append(my_str[i:i+n])
    else:
        for i in range(0, len(my_str), n):
            if i + n < len(my_str):
                answer.append(my_str[i:i+n])
            else:
                answer.append(my_str[i:])
    return answer