def solution(nums):
    answer = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j +1, len(nums)):
                total = nums[i] + nums[j] + nums[k]
                is_Prime = True
                
                for n in range(2, total):
                    if total % n == 0:
                        is_Prime = False
                        break
                if is_Prime:
                    answer += 1
    return answer