from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi]
        represent the start and the end of the ith interval and intervals is sorted in ascending order by starti.
        You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

        Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals
        still does not have any overlapping intervals (merge overlapping intervals if necessary).

        Return intervals after the insertion.
        """
        intervals.append(newInterval)
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


intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]

s = Solution()
result = s.insert(intervals, newInterval)
print(result)