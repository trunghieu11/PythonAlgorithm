import heapq

def correctSolution(A, k):
    heap = []
    # push all value from A to heap
    for i in range(len(A)):
        # the first value of each element in heap is value
        # the second value is index in A
        heapq.heappush(heap, [A[i], i])

    # while we didn't meet k-th element
    i = 0
    while i < k - 1:
        i += 1
        # get top of heap, the smallest one
        top = heapq.heappop(heap)
        value = top[0]
        index = top[1]
        # push to heap new element after increase it
        heapq.heappush(heap, [value + A[index], index])

    # now we meet the k-th smallest multiple
    answer = heapq.heappop(heap)
    return answer[0]