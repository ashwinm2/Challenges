# Minimum Path
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        length = len(grid)
        if length < 2:
            if length == 0:
                return 0
            else:
                index = len(grid[0])
                for x in range(1,index):
                    grid[0][x] += grid[0][x - 1]
                return grid[0][-1]
        else:
            index = len(grid[0])
            for x in range(1,index):
                grid[0][x] += grid[0][x - 1]
            
            jndex = len(grid)
            for x in range(1, jndex):
                grid[x][0] += grid[x - 1][0]
            
            
            for x in range(1, jndex):
                for y in range(1,index):
                    grid[x][y] += self.low(grid[x - 1][y],grid[x][y - 1])
            
            return grid[-1][-1]
    
    def low(self, x, y):
        if x < y:
            return x
        else:
            return y