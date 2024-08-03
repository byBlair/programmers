def solution(nums):
    poketmon= len(set(nums))
    max_select = len(nums) // 2
    return min(poketmon, max_select)