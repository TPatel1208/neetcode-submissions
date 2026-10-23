class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        cols = len(grid[0])
        rows = len(grid)
        seen = set()
        islands = 0
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        queue = collections.deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in seen:
                    seen.add((r,c))
                    queue.append((r,c))
                    while queue:
                        r,c = queue.popleft()
                        for ro, co in directions:
                            row = r+ro
                            col = c+co
                            if (row in range(rows) and 
                            col in range(cols) and
                            (row,col) not in seen and grid[row][col]=='1'):
                                queue.append((row,col))
                                seen.add((row,col))
                    islands+=1
        return islands
                    
