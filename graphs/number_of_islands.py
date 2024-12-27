# leetcode 200
# https://leetcode.com/problems/number-of-islands/description/



class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        # bfs
        # time complexity - O(m * n)
        # space complexity - O(m * n) how?
                
        from collections import deque

        num_islands = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(r, c):
            q = deque()
            
            # modify current element and add it to the queue to modify its neighbours
            grid[r][c] = "0"
            q.append((r, c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc

                    # setup boundary conditions for the BFS to stop traversing
                    if (
                        new_row < 0 
                        or new_col < 0 
                        or new_row >= ROWS 
                        or new_col >= COLS 
                        or grid[new_row][new_col] == "0"
                    ):
                        continue 

                    # modify neighbour and add it to the queue
                    grid[new_row][new_col] = "0"
                    q.append((new_row, new_col))

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    bfs(row, col)
                    num_islands += 1

        return num_islands