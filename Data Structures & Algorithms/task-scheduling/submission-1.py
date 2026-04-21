import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_heap = [-cnt for cnt in counts.values()]
        heapq.heapify(max_heap)

        wait_queue = deque()
        result_res = []
        time = 0
        while max_heap or wait_queue:
            time += 1
            if max_heap:
                cnt = heapq.heappop(max_heap) + 1
                if cnt < 0:
                    wait_queue.append((cnt, time + n))
                result_res.append('Task')
            else:
                result_res.append("Idle")
            
            if wait_queue and wait_queue[0][1] == time:
                heapq.heappush(max_heap, wait_queue.popleft()[0])

        return time
