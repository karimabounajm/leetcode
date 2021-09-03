from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def helper(grid, i, j):
            if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] != '1':
              return 
            grid[i][j] = "0" 
            helper(grid, i, j + 1)
            helper(grid, i, j - 1)
            helper(grid, i + 1, j)
            helper(grid, i - 1, j)
        numOfIslands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "0":
                    continue
                numOfIslands += 1
                helper(grid, i, j)
        return numOfIslands

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]]
sol = Solution()
print(sol.numIslands(grid))