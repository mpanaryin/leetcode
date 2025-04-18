from collections import defaultdict


def fn(arr, k):
    """
    Find number of subarrays that fit an exact criteria
    """
    counts = defaultdict(int)
    counts[0] = 1
    ans = curr = 0
    for num in arr:
        # do logic to change curr
        ans += counts[curr - k]
        counts[curr] += 1
    return ans
