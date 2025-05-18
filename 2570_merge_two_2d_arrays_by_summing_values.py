class Solution:
    """
    Grade[Easy]
    Topics[Array, Hash Table, Two Pointers]

    You are given two 2D integer arrays nums1 and nums2.

    nums1[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
    nums2[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
    Each array contains unique ids and is sorted in ascending order by id.

    Merge the two arrays into one array that is sorted in ascending order by id,
    respecting the following conditions:

    Only ids that appear in at least one of the two arrays should be included in the resulting array.
    Each id should be included only once and its value should be the sum of the values of this id in the two arrays.
    If the id does not exist in one of the two arrays, then assume its value in that array to be 0.
    Return the resulting array. The returned array must be sorted in ascending order by id.

    Constraints:

    1 <= nums1.length, nums2.length <= 200
    nums1[i].length == nums2[j].length == 2
    1 <= idi, vali <= 1000
    Both arrays contain unique ids.
    Both arrays are in strictly ascending order by id.
    """

    def mergeArrays(self, nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
        """
        Time complexity: O(n + m)
        Space complexity: O(n + m)
        """
        length1 = len(nums1)
        length2 = len(nums2)
        i = j = 0
        result = []
        # Через два указателя добавляем элементы
        while i != length1 and j != length2:
            if nums1[i][0] == nums2[j][0]:
                result.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                i += 1
                j += 1
            elif nums1[i][0] < nums2[j][0]:
                result.append(nums1[i])
                i += 1
            elif nums1[i][0] > nums2[j][0]:
                result.append(nums2[j])
                j += 1
        # Так как размер массивов может быть разный, нужно добавить оставшуюся часть (если она есть)
        if i != length1:
            result.extend(nums1[i:])
        elif j != length2:
            result.extend(nums2[j:])
        return result


s = Solution()
nums1 = [[2, ], [3, 6], [5, 5]]
nums2 = [[1, 3], [4, 3]]
print(s.mergeArrays(nums1, nums2))
