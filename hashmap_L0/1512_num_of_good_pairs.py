class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = {}
        ans = 0

        for num in nums:
            ans += count.get(num, 0)
            count[num] = count.get(num, 0) + 1

        return ans
    
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hm = {}
        res = 0
        for i in range(len(nums)):
            if nums[i] not in hm:
                hm[nums[i]] = 1
            else:
                hm[nums[i]] += 1
        for value in hm.values():
            if value == 1:
                continue
            else:
                res += (value * (value -1)) // 2
        return res