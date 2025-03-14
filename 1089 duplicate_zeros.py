class Solution:
    """
    Given a fixed-length integer array arr, duplicate each occurrence of zero,
    shifting the remaining elements to the right.

    Note that elements beyond the length of the original array are not written.
    Do the above modifications to the input array in place and do not return anything.

    Constraints:
    1 <= arr.length <= 10^4
    0 <= arr[i] <= 9
    """
    def duplicate_zeros(self, arr: list[int]) -> None:
        """
        Моё решение: срез будет O(n), где n - количество элементов в срезе
        Time Complexity: O(N*M), где M количество срезов, худший случай O(N^2)
        Space Complexity: O(1)
        """
        length = len(arr)
        i = 0
        while i < length - 1:
            if arr[i] == 0:
                arr[i+2:length] = arr[i+1:length-1]
                arr[i+1] = 0
                i += 1
            i += 1

    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Рекомендуемое решение:
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        possible_dups = 0
        length_ = len(arr) - 1

        # Find the number of zeros to be duplicated
        for left in range(length_ + 1):

            # Stop when left points beyond the last element in the original list
            # which would be part of the modified list
            if left > length_ - possible_dups:
                break

            # Count the zeros
            if arr[left] == 0:
                # Edge case: This zero can't be duplicated. We have no more space,
                # as left is pointing to the last element which could be included
                if left == length_ - possible_dups:
                    arr[length_] = 0  # For this zero we just copy it without duplication.
                    length_ -= 1
                    break
                possible_dups += 1

        # Start backwards from the last element which would be part of new list.
        last = length_ - possible_dups
        # Copy zero twice, and non zero once.
        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i + possible_dups] = 0
                possible_dups -= 1
                arr[i + possible_dups] = 0
            else:
                arr[i + possible_dups] = arr[i]


arr1 = [1, 0, 2, 3, 0, 4, 5, 0]
arr2 = [0, 1, 7, 6, 0, 2, 0, 7]
arr3 = [1, 5, 2, 0, 6, 8, 0, 6, 0]
s = Solution()
result = s.duplicateZeros(arr3)
print(arr3)