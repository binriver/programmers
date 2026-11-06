def solution(myString):
    myString = list(myString)
    for idx, i in enumerate(myString):
        if i == "a" or i == "A":
            myString[idx] = myString[idx].upper()
        else:
            myString[idx] = myString[idx].lower()
    return "".join(myString)