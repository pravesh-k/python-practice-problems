## This problem is from LeetCode numbered #695. Max Area of Island

# Problem Statement: You are given an m x n binary matrix grid. An island is a 
# group of 1's (representing land) connected 4-directionally (horizontal or 
# vertical.) You may assume all four edges of the grid are surrounded by water.
# The area of an island is the number of cells with a value 1 in the island. 
# Return the maximum area of an island in grid. If there is no island, return 0.

# Costraints:
# rows == grid.length
# cols == grid[i].length
# 1 <= rows, cols <= 50
# grid[i][j] is only either 0 or 1


from typing import List
from itertools import product

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        # find rows, cols, and assume max value of area of any island be 0
        rows, cols, area = len(grid), len(grid[0]), 0
        
        # recursive function to traverse all cells of grid and calculate the 
        # area of each island
        def dfs(i, j):
            nonlocal grid, rows, cols
            
            # if below conditions are true, area will not be incremented to 1 unit
            if i<0 or i>=rows or j<0 or j>=cols or grid[i][j] == 0:
                return 0
            
            # to mark the visited cell, change the value of cell from 1 to 0
            grid[i][j] = 0

            # calculate the unit area of 4 directional neighbours and add to area
            return 1 + dfs(i-1, j) + dfs(i+1, j) + dfs(i, j-1) + dfs(i, j+1)
            
        # traverse each cell and when a cell with value 1 detected find the area 
        # of island associated with the cell
        for i, j in product(range(rows), range(cols)):
            if grid[i][j]:
                area = max(area, dfs(i,j))          # compare the area of current island's area to last value
                
        return area

# driver code
def main():

    sol = Solution()
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,
    0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0
    ],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

    print(sol.maxAreaOfIsland(grid))


if __name__ == "__main__":
    main()
