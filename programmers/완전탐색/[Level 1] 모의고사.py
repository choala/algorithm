def solution(answers):
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    score = [0 for _ in range(3)]
    
    for i in range(len(answers)):
        if p1[i % len(p1)] == answers[i]:
            score[0] += 1
        if p2[i % len(p2)] == answers[i]:
            score[1] += 1
        if p3[i % len(p3)] == answers[i]:
            score[2] += 1
            
    return [i + 1 for i in range(len(score)) if score[i] == max(score)]
