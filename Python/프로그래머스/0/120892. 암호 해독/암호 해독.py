def solution(cipher, code):
    answer = [cipher[k-1] for k in range(code, len(cipher)+1, code)]
    return "".join(answer)