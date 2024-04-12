def solution(nums):
    selected = []
    
    index = 0
    while len(selected) < len(nums) // 2 and index < len(nums):
        if nums[index] not in selected:
            selected.append(nums[index])
            
        index += 1
        
    return len(selected)
