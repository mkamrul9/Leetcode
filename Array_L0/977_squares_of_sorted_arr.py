class Solution:
    def sortedSquares(nums):

        n = len(nums)

        res = [0] * n

        l = 0
        r = n - 1

        pos = n - 1

        while l <= r:

            if abs(nums[l]) > abs(nums[r]):
                res[pos] = nums[l] * nums[l]
                l += 1
            else:
                res[pos] = nums[r] * nums[r]
                r -= 1

            pos -= 1

        return res