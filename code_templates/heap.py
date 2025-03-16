import heapq

CRITERIA = 'CRITERIA'


def fn(arr, k):
    """
    Find top k elements with heap
    """
    heap = []
    for num in arr:
        # do some logic to push onto heap according to problem's criteria
        heapq.heappush(heap, (CRITERIA, num))
        if len(heap) > k:
            heapq.heappop(heap)

    return [num for num in heap]