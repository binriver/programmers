def solution(my_string, is_prefix):
    l = len(is_prefix)
    if my_string[:l] == is_prefix:
        answer = 1
    else:
        answer = 0
    return answer