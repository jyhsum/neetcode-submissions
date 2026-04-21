class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        m, n = len(heights), len(heights[0])

        def dfs(r, c, visited):
            visited.add((r, c))
            for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nr, nc = r + dr, c + dc
                if nr in range(m) and nc in range(n) and (nr, nc) not in visited and heights[nr][nc] >=  heights[r][c]:
                    dfs(nr, nc, visited)
        

        for r in range(m):
            dfs(r, 0, pacific)
        for c in range(n):
            dfs(0, c, pacific)
        for r in range(m):
            dfs(r, n - 1, atlantic)
        for c in range(n):
            dfs(m - 1, c, atlantic)
        
        return list(pacific & atlantic)