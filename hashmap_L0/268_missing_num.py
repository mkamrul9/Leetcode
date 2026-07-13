class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = (n * (n + 1)) / 2
        arr_sum = sum(nums)
        return int(total - arr_sum)
    
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i not in nums: return i
        return len(nums)