def solution(sizes):
    max_w = 0
    max_h = 0
    
    for w, h in sizes:
        if w < h:
            w, h = h, w
            
        if max_w < w:
            max_w = w
        if max_h < h:
            max_h = h
    
    return max_w * max_h
