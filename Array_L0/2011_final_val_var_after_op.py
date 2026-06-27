class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0

        for op in operations:
            if op.startswith("+") or op.endswith("+"):
                x += 1
            else:
                x -= 1

        return x