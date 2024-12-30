# leetcode 695
# https://leetcode.com/problems/max-area-of-island/description/

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        # dfs
        # time complexity: O(m * n)
        # space complexity: O(m * n)
        max_area = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            area = 0
        
            # define the base case since dfs is recursive
            if (
                r < 0
                or c < 0
                or r >= ROWS
                or c >= COLS
                or grid[r][c] == 0
            ):
                return area

            # do the node modification
            area += 1
            grid[r][c] = 0

            # loop through the directions and call dfs 
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)

            return area

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    area = dfs(row, col)
                    max_area = max(max_area, area)

        return max_area


    def _maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        # bfs
        # time complexity: O(m * n)
        # space complexity: O(m * n) how?
        max_area = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])

        from collections import deque

        def bfs(r, c):
            area = 0
            q = deque()

            area += 1
            grid[r][c] = 0
            q.append((r, c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    new_r, new_c = row + dr, col + dc

                    if (
                        new_r < 0
                        or new_c < 0
                        or new_r >= ROWS
                        or new_c >= COLS
                        or grid[new_r][new_c] == 0
                    ):
                        continue

                    area += 1
                    grid[new_r][new_c] = 0
                    q.append((new_r, new_c))

            return area

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    area = bfs(row, col)
                    max_area = max(max_area, area)
        
        return max_area