class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        seen = [False] * 26

        for ch in sentence:
            seen[ord(ch) - ord('a')] = True

        return all(seen)
    

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26