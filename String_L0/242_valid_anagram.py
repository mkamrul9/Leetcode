class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        return Counter(s) == Counter(t)
    
# if the problem only contains lowercase english letter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26

        for c1, c2 in zip(s, t):
            count[ord(c1) - ord('a')] += 1
            count[ord(c2) - ord('a')] -= 1

        return all(x == 0 for x in count)