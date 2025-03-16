import math
from collections import Counter
from heapq import heapify, heappop, heappush


class Solution:
    """
    Grade [Medium]

    You are given an integer array ranks representing the ranks of some mechanics.
    ranksi is the rank of the ith mechanic. A mechanic with a rank r can repair n cars in r * n2 minutes.

    You are also given an integer cars representing the total number of cars waiting in the garage to be repaired.

    Return the minimum time taken to repair all the cars.

    Note: All the mechanics can repair the cars simultaneously.

    Constraints:
    1 <= ranks.length <= 10^5
    1 <= ranks[i] <= 100
    1 <= cars <= 10^6
    """
    def repairCars(self, ranks: list[int], cars: int) -> int:
        """
        Time Complexity: O(n+max_rank log(m*max_rank))
        Space Complexity: O(max_rank)
        """
        min_rank, max_rank = ranks[0], ranks[0]
        # Find min and max rank dynamically
        for rank in ranks:
            min_rank = min(min_rank, rank)
            max_rank = max(max_rank, rank)
        # Frequency list to count mechanics with each rank
        freq = [0] * (max_rank + 1)
        for rank in ranks:
            min_rank = min(min_rank, rank)
            freq[rank] += 1
        # Minimum possible time, Maximum possible time
        low = 1
        high = min_rank * cars * cars
        # Perform binary search to find the minimum time required
        while low < high:
            mid = (low + high) // 2
            cars_repaired = 0
            # Calculate the total number of cars that can be repaired in 'mid' time
            for rank in range(1, max_rank + 1):
                cars_repaired += freq[rank] * int(math.sqrt(mid // rank))
            # Adjust the search boundaries based on the number of cars repaired
            if cars_repaired >= cars:
                high = mid  # Try to find a smaller time
            else:
                low = mid + 1  # Need more time
        return low

    def repairCars(self, ranks: list[int], cars: int) -> int:
        """
        Time Complexity: O(n⋅log(m⋅max_rank))
        Space Complexity: O(1)
        """
        # The minimum possible time is 1,
        # and the maximum possible time is when the slowest mechanic (highest rank) repairs all cars.
        low, high = 1, cars * cars * ranks[0]
        # Perform binary search to find the minimum time required.
        while low < high:
            mid = (low + high) // 2
            cars_repaired = sum(int((mid / rank) ** 0.5) for rank in ranks)
            # If the total cars repaired is less than required, increase the time.
            if cars_repaired < cars:
                low = mid + 1
            else:
                high = mid  # Otherwise, try a smaller time.
        return low

    def repairCars(self, rank: list[int], cars: int) -> int:
        """
        Time Complexity: O(n+mlogk)
        Space Complexity: O(k)
        """
        # Count the frequency of each rank using a Counter
        count = Counter(rank)
        # Create a Min-heap storing [time, rank, n, count]:
        # - time: time for the next repair
        # - rank: mechanic's rank
        # - n: cars repaired by this mechanic
        # - count: number of mechanics with this rank
        # Initial time = rank (as rank * 1^2 = rank)
        min_heap = [[rank, rank, 1, count[rank]] for rank in count]
        heapify(min_heap)
        # Process until all cars are repaired
        while cars > 0:
            # Pop the mechanic with the smallest current repair time
            time, rank, n, count = heappop(min_heap)
            # Deduct the number of cars repaired by this mechanic group
            cars -= count
            # Increment the number of cars repaired by this mechanic
            n += 1
            # Push the updated repair time back into the heap
            # The new repair time is rank * n^2 (since time increases quadratically with n)
            heappush(min_heap, [rank * n * n, rank, n, count])
        return time


ranks = [4, 2, 3, 1]
cars = 10
s = Solution()
result = s.repairCars(ranks, cars)
print(result)
