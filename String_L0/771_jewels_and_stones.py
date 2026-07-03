class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for char in stones:
            if char in jewels:
                count += 1
        return count
# not optimal

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(jewels)
        return sum(char in jewels for char in stones)
# optimal this one