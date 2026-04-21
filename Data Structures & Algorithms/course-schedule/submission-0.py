class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0] * numCourses
        graph = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            graph[b].append(a) #b上完就可以上a
            in_degree[a] += 1 # 上a之前有幾堂前置課
        
        q = deque(i for i in range(numCourses) if in_degree[i] == 0)
        count = 0
        while q:
            n = q.popleft()
            count += 1
            for nxt_class in graph[n]:
                in_degree[nxt_class] -= 1
                if in_degree[nxt_class] == 0:
                    q.append(nxt_class)
        return count == numCourses