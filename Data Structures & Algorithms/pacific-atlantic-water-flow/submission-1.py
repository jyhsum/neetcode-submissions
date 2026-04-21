class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(q, visited):
            while q:
                r, c = q.popleft()
                visited.add((r, c))
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr in range(ROWS) and nc in range(COLS) and (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]):
                        
                        q.append((nr, nc))
        
        atl = deque()
        pac = deque()
        pac_visited = set()
        atl_visited = set()
        for r in range(ROWS):
            pac.append((r, 0))
            atl.append((r, COLS - 1))
        for c in range(COLS):
            pac.append((0, c))
            atl.append((ROWS - 1, c))

        bfs(pac, pac_visited)
        bfs(atl, atl_visited)

        return list(pac_visited & atl_visited)
