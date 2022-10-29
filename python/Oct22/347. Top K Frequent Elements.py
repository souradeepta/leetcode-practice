from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int, type=0) -> list[int]:
        """return k most frequent numbers from nums

        Args:
            nums (list[int]): _description_
            k (int): _description_

        Returns:
            list[int]: _description_
        Complexity:
            type0 Time O(nlogn) of most_common sorted heapq operation
            type1 Time O(n) and space O(n)
            type1, imagine buckets of counts possible,
            highest count can be len(nums)+1 eg. [4,4,4,4,4,4,1]
            now count numbers and put them in those buckets[6:[4], 1:[1]]
        """
        if type == 0:
            frequency = Counter(nums).most_common(k)
            return [x[0] for x in frequency]
        else:
            # neetcode
            count = {}
            freq = [[] for i in range(len(nums) + 1)]

            for n in nums:
                count[n] = 1 + count.get(n, 0)

            for n, c in count.items():
                freq[c].append(n)

            topKFreq = []

            for i in range(len(freq) - 1, 0, -1):
                for n in freq[i]:
                    topKFreq.append(n)
                    if len(topKFreq) == k:
                        return topKFreq


if __name__ == "__main__":
    s = Solution()
    assert s.topKFrequent([1], 1) == [1]
    assert s.topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
    assert s.topKFrequent([1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3], 2) == [3, 1]
    assert s.topKFrequent([1, 1, 1, 2, 2, 3], 2, type=1) == [1, 2]
