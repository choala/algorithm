def solution(participant, completion):
    p = sorted(participant)
    c = sorted(completion)
    
    for i in range(len(c)):
        if not p[i] == c[i]:
            return p[i]
        
    return p[len(p) - 1]
