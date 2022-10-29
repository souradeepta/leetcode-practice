from collections import Counter


class Solution:
    def containsDuplicate(self, nums: list[int], type=0) -> bool:
        """count duplicates in array

        Args:
            nums (list[int]):
            type: type of data structure to use

        Returns:
            bool:
        Complexity:
            Time O(n)
            Space O(n)
        """
        if type == 0:
            count = Counter(nums)
            highest_freq = count.most_common(1)[0]
            if highest_freq[1] > 1:
                return True
            else:
                return False
        else:
            # neetcode sol
            hashset = set()
            for n in nums:
                if n in hashset:
                    return True
                hashset.add(n)
            return False


if __name__ == "__main__":
    s = Solution()
    assert s.containsDuplicate([1, 2, 3, 1]) is True
    assert s.containsDuplicate([1, 2, 3, 4]) is False
    assert s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True
    assert s.containsDuplicate([1, 2, 3, 1], type=1) is True
