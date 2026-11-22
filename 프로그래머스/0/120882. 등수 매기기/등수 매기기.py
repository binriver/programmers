def solution(score):
    avg = [sum(s)/2 for s in score]
    ranks = sorted(avg, reverse=True)
    return [ranks.index(i)+1 for i in avg]
        
    
            