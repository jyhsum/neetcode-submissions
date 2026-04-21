class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adj = [[] for _ in range(n)]

        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)

        q = deque()
        in_degree = [0] * n
        for src, nei in enumerate(adj):
            in_degree[src] = len(nei)
            if len(nei) == 1:
                q.append(src)
        
        while q:
            if n <= 2:
                return list(q)
            for _ in range(len(q)):
                node = q.popleft()
                n -= 1
                for nei in adj[node]:
                    in_degree[nei] -= 1
                    if in_degree[nei] == 1:
                        q.append(nei)






            