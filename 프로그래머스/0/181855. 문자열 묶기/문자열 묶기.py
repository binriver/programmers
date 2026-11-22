def solution(strArr):
    m_dict = {}
    for l in range(1, 31):
        m_dict[l] = 0
        
    for i in strArr:
        m_dict[len(i)] += 1
        
    return max(m_dict.values())