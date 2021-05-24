class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        result = [first]
        if not encoded:
            return result
        for ele in encoded:
            result.append(ele ^ first)
            first = result[-1]
        return result
