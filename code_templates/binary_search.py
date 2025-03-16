MINIMUM_POSSIBLE_ANSWER = object
MAXIMUM_POSSIBLE_ANSWER = object


def fn(arr, target):
    """
    Binary search
    """
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            # do something
            return
        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    # left is the insertion point
    return left


def fn(arr, target):
    """
    Binary search: duplicate elements, left-most insertion point
    """
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return left


def fn(arr, target):
    """
    Binary search: duplicate elements, right-most insertion point
    """
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid
        else:
            left = mid + 1
    return left


def fn(arr):
    """
    Binary search: for greedy problems

    If looking for a minimum:
    """
    def check(x):
        # this function is implemented depending on the problem
        return bool

    left = MINIMUM_POSSIBLE_ANSWER
    right = MAXIMUM_POSSIBLE_ANSWER
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            right = mid - 1
        else:
            left = mid + 1
    return left


def fn(arr):
    """
    Binary search: for greedy problems
    
    If looking for a maximum:
    """
    def check(x):
        # this function is implemented depending on the problem
        return bool

    left = MINIMUM_POSSIBLE_ANSWER
    right = MAXIMUM_POSSIBLE_ANSWER
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            left = mid + 1
        else:
            right = mid - 1
    return right