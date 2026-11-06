def solution(strArr):
    for idx, i in enumerate(strArr):
        if idx % 2:
            strArr[idx] = strArr[idx].upper()
        else:
            strArr[idx] = strArr[idx].lower()
    return strArr