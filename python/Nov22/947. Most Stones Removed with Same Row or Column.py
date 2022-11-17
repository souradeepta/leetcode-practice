from collections import defaultdict


class Solution:
    """Daily challenege 11-13"""

    def removeStones(self, stones):
        def dfs(i, j):
            points.discard((i, j))
            for y in rows[i]:
                if (i, y) in points:
                    dfs(i, y)
            for x in cols[j]:
                if (x, j) in points:
                    dfs(x, j)

        points = {(i, j) for i, j in stones}
        island = 0
        rows, cols = (
            defaultdict(list),
            defaultdict(list),
        )
        for i, j in stones:
            rows[i].append(j)
            cols[j].append(i)
        for i, j in stones:
            if (i, j) in points:
                dfs(i, j)
                island += 1
        return len(stones) - island

    def deprecated_removeStones(self, stones: list[list[int]]) -> int:
        total_stones = len(stones)
        x_map, y_map = defaultdict(list), defaultdict(list)
        for ele in stones:
            if ele[0] in x_map.keys():
                # x_map.get(ele[0]).append(ele)
                continue
            else:
                x_map[ele[0]] = ele
        x_filter = list(x_map.values())

        for ele in x_filter:
            if ele[1] in y_map.keys():
                # x_map.get(ele[0]).append(ele)
                continue
            else:
                y_map[ele[1]] = ele
        print(y_map)
        removed = total_stones - len(y_map.values())
        return removed
        # for ele in stones:
        #     if ele[1] in y_map.keys():
        #         x_map.get(ele[1]).append(ele)
        #     else:
        #         x_map[ele[1]] = ele

        # for

        pass


s = Solution()
assert s.removeStones([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]) == 5
assert s.removeStones([[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]) == 3
