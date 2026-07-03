
def rotate(nums, k):
    n = len(nums)
    k %= n
    res = [0] * n
    for i in range(n):
        res[(i + k) % n] = nums[i]
    nums[:] = res
# no optimal as space o(n)


# class Solution:
#     def rotate(nums, k):
#         k %= len(nums)
#         nums.reverse()
#         nums[:k] = reversed(nums[:k])
#         nums[k:] = reversed(nums[k:])