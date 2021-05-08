'''
Given a 2-dimensional grid of integers, each value in the grid represents the color of the grid 
square at that location.

Two squares belong to the same connected component if and only if they have the same color and are 
next to each other in any of the 4 directions.

The border of a connected component is all the squares in the connected component that are either 
4-directionally adjacent to a square not in the component, or on the boundary of the grid (the first 
or last row or column).

Given a square at location (r0, c0) in the grid and a color, color the border of the connected component 
of that square with the given color, and return the final grid.

 

Example 1:

Input: grid = [[1,1],[1,2]], r0 = 0, c0 = 0, color = 3
Output: [[3, 3], [3, 2]]
Example 2:

Input: grid = [[1,2,2],[2,3,2]], r0 = 0, c0 = 1, color = 3
Output: [[1, 3, 3], [2, 3, 3]]
Example 3:

Input: grid = [[1,1,1],[1,1,1],[1,1,1]], r0 = 1, c0 = 1, color = 2
Output: [[2, 2, 2], [2, 1, 2], [2, 2, 2]]
 

Note:

1 <= grid.length <= 50
1 <= grid[0].length <= 50
1 <= grid[i][j] <= 1000
0 <= r0 < grid.length
0 <= c0 < grid[0].length
1 <= color <= 1000
'''

def color_the_border(grid, r0, c0, color):
    exptected_color, components = grid[r0][c0], set()
    
    def neighbors(i, j):
        nei = []
        directions = [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]
        for x, y in directions:
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                nei.append((x, y))
        return nei 

    def dfs(i, j, seen):
        nonlocal components
        seen.add((i, j))
        nei = neighbors(i, j)
        if i == 0 or i == len(grid) - 1 or j == 0 or j == len(grid[0]) - 1:
            components.add((i, j))
        for x, y in nei:
            if grid[x][y] != exptected_color:
                components.add((i, j))
            if grid[x][y] == exptected_color and (x, y) not in seen:
                dfs(x, y, seen)
    
    dfs(r0, c0, set())
    for i, j in components:
        grid[i][j] = color 

    return grid 


