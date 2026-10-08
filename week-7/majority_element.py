def majority_elment(nums):
    for num in nums:
        if nums.count(num) >= len(nums) / 2:
            return num


print(majority_elment([3, 2, 3]))
print(majority_elment([2, 2, 1, 1, 1, 2, 2]))
print(majority_elment([2, 2, 3, 2, 1, 2, 1, 4, 4, 1, 2, 2]))
