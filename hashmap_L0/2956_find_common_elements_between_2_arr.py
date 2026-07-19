class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set(nums1)
        s2 = set(nums2)

        ans1 = 0
        ans2 = 0

        for num in nums1:
            if num in s2:
                ans1 += 1

        for num in nums2:
            if num in s1:
                ans2 += 1

        return [ans1, ans2]