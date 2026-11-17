def solution(spell, dic):
    spell = sorted(spell)
    
    for d in dic:
        if sorted(list(d)) == spell:
            return 1
    return 2