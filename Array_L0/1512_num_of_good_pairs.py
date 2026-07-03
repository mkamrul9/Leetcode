
def numIdenticalPairs(nums):
    count = {}
    ans = 0

    for num in nums:
        ans += count.get(num, 0)
        count[num] = count.get(num, 0) + 1

    return ans