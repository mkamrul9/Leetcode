def longest_consecutive_sequence(nums):
    if not nums:
        return 0

    nums.sort()

    count = 1
    result = 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            continue
        elif nums[i] == nums[i-1] + 1:
            count += 1
        else:
            result = max(result, count)
            count = 1

    return max(result, count) 
#instead of returning result we return max because if the array is alrewady the longest sequence it wont give correct result
# this one O(nlogn) nad O(1)

# we can do it in O(n), but space will also be O(n)

# Optimal solution
def longest_consecutive_sequence(nums):
    nums_set = set(nums)
    longest = 0

    for num in nums_set:
        if num - 1 not in nums_set:  # start of sequence
            length = 1

            while num + length in nums_set:
                length += 1

            longest = max(longest, length)

    return longest