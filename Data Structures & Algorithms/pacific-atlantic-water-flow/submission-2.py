class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(q, visited):
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr in range(ROWS) and nc in range(COLS) and (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]):
                        visited.add((nr, nc))
                        q.append((nr, nc))
        
        atl = deque()
        pac = deque()
        pac_visited = set()
        atl_visited = set()
        for r in range(ROWS):
            pac.append((r, 0))
            pac_visited.add((r, 0))
            atl.append((r, COLS - 1))
            atl_visited.add((r, COLS - 1))
        for c in range(COLS):
            pac.append((0, c))
            pac_visited.add((0, c))
            atl.append((ROWS - 1, c))
            atl_visited.add((ROWS - 1, c))

        bfs(pac, pac_visited)
        bfs(atl, atl_visited)

        return list(pac_visited & atl_visited)
