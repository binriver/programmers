def solution(myString, pat):
    pat = pat.upper()
    myString = myString.upper()
    return 1 if pat in myString else 0