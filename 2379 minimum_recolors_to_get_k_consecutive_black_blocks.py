class Solution:
    """
    You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B',
    representing the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.

    You are also given an integer k, which is the desired number of consecutive black blocks.

    In one operation, you can recolor a white block such that it becomes a black block.

    Return the minimum number of operations needed such that there is
    at least one occurrence of k consecutive black blocks.

    n == blocks.length
    1 <= n <= 100
    blocks[i]либо 'W', либо 'B'.
    1 <= k <= n
    """

    def minimumRecolors(self, blocks: str, k: int) -> int:
        minimum = k
        for i in range(len(blocks) - k + 1):
            res = blocks[i:i+k].count('W')
            if res < minimum:
                minimum = res
        return minimum

blocks = "BWWWBB"
k = 6

s = Solution()
r = s.minimumRecolors(blocks, k)
print(r)