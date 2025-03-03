from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
        and return an array of the non-overlapping intervals that cover all the intervals in the input.
        """
        intervals.sort()
        intervals_len = len(intervals)
        counter = 0
        for i in range(intervals_len - 1):
            current_index = i - counter
            if intervals[current_index + 1][0] <= intervals[current_index][1] <= intervals[current_index + 1][1]:
                intervals[current_index + 1][0] = intervals[current_index][0]
                if intervals[current_index][1] > intervals[current_index + 1][1]:
                    intervals[current_index + 1][1] = intervals[current_index][1]
                del intervals[current_index]
                counter += 1
            elif intervals[current_index + 1][0] <= intervals[current_index][1] >= intervals[current_index + 1][1]:
                del intervals[current_index + 1]
                counter += 1
        return intervals


intervals = [[1,4],[2,3]]
s = Solution()
result = s.merge(intervals)
print(result)
