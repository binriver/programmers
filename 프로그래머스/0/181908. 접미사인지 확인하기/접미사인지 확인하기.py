def solution(my_string, is_suffix):
    l = len(is_suffix)
    if my_string[-l:] == is_suffix:
        answer = 1
    else:
        answer = 0
    return answer