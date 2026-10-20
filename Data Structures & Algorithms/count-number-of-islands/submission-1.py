class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        seen = set()
        islands = 0 
        rows = len(grid)
        cols = len(grid[0])
        
        def bfs(r,c):
            queue = collections.deque()
            queue.append((r,c))
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            while queue:
                r,c = queue.popleft()
                for ro,co in directions:
                    row = r+ro
                    col = c+co
                    if (row in range(rows) and 
                    col in range(cols) and 
                    grid[row][col] == '1' and 
                    (row,col) not in seen):
                        seen.add((row,col))
                        queue.append((row,col))



        for r in range(rows):  
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in seen:
                    seen.add((r,c))
                    bfs(r,c)
                    islands += 1

        
        return islands