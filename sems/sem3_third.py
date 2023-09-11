nums = [1, 1, 2, 2, 2, 3, 4, 5, 8, 9, 9, 10, 10, 10, 10]
nums_origin = []

for item in nums:
    if nums.count(item) % 2 == 1:
        nums_origin.append(item)
print(nums_origin)
