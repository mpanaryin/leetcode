def fn(arr):
    """
    Monotonic increasing stack

    The same logic can be applied to maintain a monotonic queue.
    """
    stack = []
    ans = 0
    for num in arr:
        # for monotonic decreasing, just flip the > to <
        while stack and stack[-1] > num:
            # do logic
            stack.pop()
        stack.append(num)
    return ans
