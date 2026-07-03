
def shuffle(nums, n):
    l = 0 
    r = n
    res = []
    while r < 2 * n:
        res.append(nums[l])
        l += 1
        res.append(nums[r])
        r += 1
    return res

# class Solution:
#     def shuffle(self, nums: List[int], n: int) -> List[int]:
#         return [x for i in range(n) for x in (nums[i], nums[i + n])]