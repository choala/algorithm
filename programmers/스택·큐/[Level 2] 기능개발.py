import math
from collections import deque

def solution(progresses, speeds):
    counts = []
    taken_days = deque()
    
    for progress, speed in zip(progresses, speeds):
        taken_day = (100 - progress) / speed
        taken_days.append(math.ceil(taken_day))

    count = 1
    target = taken_days.popleft()
    for taken_day in taken_days:
        if taken_day <= target:
            count += 1
        else:
            target = taken_day
            counts.append(count)
            count = 1
    
    counts.append(count)
    
    return counts
        
