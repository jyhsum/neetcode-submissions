class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        max_area = 0
        visited = set()

        def _dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0 or (r, c) in visited):
                return 0
            visited.add((r, c))
    
            cur_area = 1
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                cur_area += _dfs(nr, nc)
            return cur_area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(max_area, _dfs(r, c))
        
        return max_area