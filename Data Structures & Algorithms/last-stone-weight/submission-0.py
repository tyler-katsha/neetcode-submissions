import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #convert to max heap using negatives
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)

            if x != y:
                heapq.heappush(heap,x - y)
        
        return -heap[0] if heap else 0
