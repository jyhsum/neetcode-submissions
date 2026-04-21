from collections import OrderedDict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        heap = []
        for num, count in freq.items():
            heapq.heappush(heap, (-count, num))
        
        top_k_elements = []
        for _ in range(k):
            top_k_elements.append(heapq.heappop(heap)[1])
        return top_k_elements


        