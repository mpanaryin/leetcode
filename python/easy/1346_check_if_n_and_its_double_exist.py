class Solution:
    """
    Grade[Easy]
    Topics[Array, Hash Table, Two Pointers, Binary Search, Sorting]

    Given an array arr of integers, check if there exist two indices i and j such that:
    i != j
    0 <= i, j < arr.length
    arr[i] == 2 * arr[j]

    Constraints:
    2 <= arr.length <= 500
    -10^3 <= arr[i] <= 10^3
    """

    def check_if_exist(self, arr: list[int]) -> bool:
        """
        Самое простое, но скорее всего самое долгое
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] * 2 == arr[j] or arr[j] * 2 == arr[i]:
                    return True
        return False

    def checkIfExist2(self, arr: list[int]) -> bool:
        """
        Неплохо, но не идеально
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if arr.count(0) >= 2:
            return True
        seen = set(arr)
        for num in seen:
            if num * 2 in seen and num != 0:
                return True
        return False

    def checkIfExist3(self, arr: list[int]) -> bool:
        """
        Лучше, но не идеально
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        seen = set()
        for num in arr:
            # Check if 2 * num or num / 2 exists in the set
            if 2 * num in seen or (num % 2 == 0 and num // 2 in seen):
                return True
            # Add the current number to the set
            seen.add(num)
        # No valid pair found
        return False

    def checkIfExist4(self, arr: list[int]) -> bool:
        """
        Идеальное
        Time Complexity: O(n log n)
        Space Complexity: O(n) or O(log n)
        """
        # Step 1: Sort the array
        arr.sort()

        for i in range(len(arr)):
            # Step 2: Calculate the target (double of current number)
            target = 2 * arr[i]
            # Step 3: Custom binary search for the target
            index = self._custom_binary_search(arr, target)
            # If the target exists and is not the same index
            if index >= 0 and index != i:
                return True
        # No valid pair found
        return False

    def _custom_binary_search(self, arr: list[int], target: int) -> int:
        left, right = 0, len(arr) - 1

        while left <= right:
            # Avoid potential overflow
            mid = left + (right - left) // 2

            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1  # Target not found


nums1 = [7, 1, 14, 11]
nums2 = [10, 2, 5, 3]
nums3 = [-2, 0, 10, -19, 4, 6, -8]
nums4 = [0, 0]
s = Solution()
result = s.checkIfExist(nums2)
print(result)
print(nums2)
