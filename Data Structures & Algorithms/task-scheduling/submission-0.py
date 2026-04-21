from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)   # Counter({'X': 2, 'Y': 2})
        max_freq = max(counts.values())

        num_max_freq = sum(1 for f in counts.values() if f == max_freq)

        ans = (n + 1) * (max_freq - 1) + num_max_freq

        return max(len(tasks), ans)