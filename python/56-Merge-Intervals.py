from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return None

        result = []

        while intervals:
            interval = 0
        # for interval in range(len(intervals)-1):
%            if intervals[interval+1][1] > intervals[interval][1] and \
                    intervals[interval+1][0] < intervals[interval][1]:
                intervals.insert(interval,
                                 [intervals[interval][0], intervals[interval+1][1]])
            # else:
            #     result.append(intervals[interval])
            #     result.append(intervals[interval+1])

            intervals.remove(intervals[interval])
            intervals.remove(intervals[interval+1])

        return result


obj = Solution()
print(f'{obj.merge(intervals =[[1, 3], [2, 6], [8, 10], [15, 18]])}')
