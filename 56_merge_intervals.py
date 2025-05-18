from typing import List


class Solution:
    """
    Grade[Medium]
    Topics[Array, Sorting]

    Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
    and return an array of the non-overlapping intervals that cover all the intervals in the input.
    """

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Time complexity: O(n log n)
        Space complexity: O(1) (если не считать сортировку, in-place)
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

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Time complexity: O(n log n)
        Space complexity: O(1)
        """
        intervals.sort(key=lambda x: x[0])
        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


intervals = [[1, 4], [2, 3]]
s = Solution()
result = s.merge(intervals)
print(result)
