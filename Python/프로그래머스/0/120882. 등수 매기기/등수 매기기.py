def solution(score):
    avg = [sum(s)/2 for s in score]
    ranks = sorted(avg, reverse=True)
    answer = []
    
    for i in avg:
        answer.append(ranks.index(i)+1)
        
    return answer
        
    
            