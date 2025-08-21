def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

def solution(nums, target):
    a = [a for a in range(len(nums))]
    b = [b for b in range(len(nums))]
    if a + b  == target:
        return [a, b]
    return []

nums = [2, 7, 11, 15]
target = 9
result = solution(nums, target)
print (result)