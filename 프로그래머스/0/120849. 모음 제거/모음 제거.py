def solution(my_string):
    for i in range(len(my_string)):
        if my_string[i] in ["a", "e", "i", "o", "u"]:
            my_string = my_string[:i] + "a" + my_string[i+1:]
    my_string = "".join(my_string.split("a"))
    return my_string