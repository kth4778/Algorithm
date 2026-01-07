def solution(nums):
    s = set()
    for num in nums:
        s.add(num)
    
    return min(len(s), len(nums)/2)