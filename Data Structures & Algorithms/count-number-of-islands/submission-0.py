class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        def bfs(row,col):
            queue = collections.deque()
            directions = [[1,0], [-1,0],[0,1],[0,-1]]
            queue.append((row,col))
            while queue:
                row, col = queue.popleft()
                for r, c in directions:
                    ro = row+r
                    co = col+c
                    if (ro in range(rows)) and (co in range(cols)) and (grid[ro][co] == '1') and (ro,co) not in seen:
                        seen.add((ro,co))
                        queue.append((ro,co))
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i,j) not in seen:
                    seen.add((i,j))
                    bfs(i,j)
                    islands +=1
        return islands


   
