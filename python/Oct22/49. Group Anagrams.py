from collections import Counter, defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str], type=0) -> list[list[str]]:
        """group the anagrams in the list of strings

        Args:
            strs (list[str]): _description_
            type (int, optional): _description_. Defaults to 0.

        Returns:
            list[list[str]]: _description_
        Complexity:
            Time O(m.n.26) ~ O(n^2) m = list of strings in str, n = length of each string
        """
        match type:
            case 0:
                groups = defaultdict(list)
                for s in strs:
                    # since set is mutable cant be a key
                    groups[frozenset(Counter(s).items())].append(s)
                return sorted(groups.values(), key=lambda x: x[0])
            case 1:
                # neetcode
                groups = defaultdict(list)
                for s in strs:
                    # char map
                    count = [] * 26
                    for c in s:
                        count[ord(c) - ord("a")] += 1
                    groups[tuple(count)].append(s)
                return sorted(groups.values(), key=len)


if __name__ == "__main__":
    s = Solution()
    assert s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [
        ["bat"],
        ["nat", "tan"],
        ["ate", "eat", "tea"],
    ]
    assert s.groupAnagrams([""]) == [[""]]
    assert s.groupAnagrams(["a"]) == [["a"]]
