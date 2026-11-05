def solution(my_string, indices):
    for i in indices:
        my_string = my_string[:i] + " "+ my_string[i+1:]
    answer = "".join(my_string.split(" "))
    return answer