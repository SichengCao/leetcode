import heapq
from collections import Counter
def findKthFrequent(nums,k):
    count = Counter(nums)
    print(nums)

    heap = []

    for value, frequency in count.items():
        heapq.heappush(heap,(frequency,value))

        if len(heap) > k:
            heapq.heappop(heap)
    result = [num for freq, num in heap]

    print(result)

def findKthLargest(nums,k):

    heap = []
    for i in range(len(nums)):
        heapq.heappush(heap,-nums[i])

        if len(heap) > k:
            heapq.heappop(heap)
    print(heap)
    print(-heap[0])


nums = [1,3,5,6,2,9,8]

findKthLargest(nums,7)


# arr = [1,1,1,3,4,3,5,5,8,8,8,8,8,0]
# findKthFrequent(arr,3)