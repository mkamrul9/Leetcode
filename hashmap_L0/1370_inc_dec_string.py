from collections import Counter

class Solution:
    def sortString(self, s: str) -> str:
        freq = Counter(s)
        keys = sorted(freq.keys())      # ['a', 'b', 'c', ...]

        ans = []

        while freq:
            # Increasing
            for ch in keys:
                if ch in freq:
                    ans.append(ch)
                    freq[ch] -= 1
                    if freq[ch] == 0:
                        del freq[ch]

            # Decreasing
            for ch in reversed(keys):
                if ch in freq:
                    ans.append(ch)
                    freq[ch] -= 1
                    if freq[ch] == 0:
                        del freq[ch]

        return "".join(ans)