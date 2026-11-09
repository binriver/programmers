def solution(date1, date2):
    
    if date1[0] - date2[0] < 0:
        return 1
    elif date1[0] - date2[0] == 0 and date1[1] - date2[1] < 0:
        return 1
    elif date1[0] - date2[0] == 0 and date1[1] - date2[1] == 0 and date1[2] - date2[2] < 0:
        return 1
    else:
        return 0