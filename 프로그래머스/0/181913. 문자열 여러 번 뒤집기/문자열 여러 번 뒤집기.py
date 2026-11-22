def solution(my_string, queries):
    my_string = list(my_string)
    for s, e in queries:
        my_string[s:e+1] = my_string[s:e+1][::-1]
    my_string = "".join(my_string)
    return my_string