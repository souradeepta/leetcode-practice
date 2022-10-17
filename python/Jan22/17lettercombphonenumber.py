from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        # bulild k:v pair dict to map digit -> letters
        d = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []
        stack = [(0, "")]
        while stack:
            i, combo = stack.pop()  # i is an index kinda of node id
            if i == len(digits):
                res.append(combo)
            else:
                nextDigit = digits[i]
                children = d[nextDigit]
                for child in children:
                    stack.append((i + 1, combo + child))
        return res
