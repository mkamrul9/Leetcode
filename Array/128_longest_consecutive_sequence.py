def longest_consecutive_sequence(nums):
    nums.sort()

    count = 1
    result = 0

    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            continue
        elif nums[i] == nums[i-1] + 1:
            count += 1
        else:
            result = max(count, result)
            count = 1 
    return result

print(longest_consecutive_sequence([100,4,200,1,3,2]))