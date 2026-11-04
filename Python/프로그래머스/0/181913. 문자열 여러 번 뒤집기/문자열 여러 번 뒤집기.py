def solution(my_string, queries):
    my_string = list(my_string)
    for k in queries:
        s, e = k[0], k[1]
        while s < e:
            my_string[s], my_string[e] = my_string[e], my_string[s]
            s += 1
            e -= 1
    my_string = "".join(my_string)
    return my_string