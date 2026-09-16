class Solution:

    def paint_around(self, i, j, grid, curr_num):
        rows = len(grid)
        cols = len(grid[0])

        # stop if out of bounds
        if i < 0 or i >= rows or j < 0 or j >= cols:
            return

        # stop if water or already painted
        if grid[i][j] != "1":
            return

        grid[i][j] = curr_num

        self.paint_around(i - 1, j, grid, curr_num)
        self.paint_around(i + 1, j, grid, curr_num)
        self.paint_around(i, j - 1, grid, curr_num)
        self.paint_around(i, j + 1, grid, curr_num)



    def numIslands(self, grid: List[List[str]]) -> int:
        
        curr_num = 2

        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):

                if grid[i][j] == "0":
                    continue

                if grid[i][j] == "1":
                    self.paint_around(i, j, grid, str(curr_num))
                    curr_num = curr_num + 1

                self.paint_around(i, j, grid, str(grid[i][j]))

        return curr_num - 2


                
