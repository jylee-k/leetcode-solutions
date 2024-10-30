class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        # keep an array to keep track of max number of moves
        m = len(grid)
        n = len(grid[0])
        move_array = [[0]*n for i in range(m)]
        
        # go through the list from the right
        for j in range(n-2, -1, -1):
            for i in range(m):
                move_array[i][j] = self.checkMoves(i,j,m,grid,move_array)
        
        return max([move_array[i][0] for i in range(m)])
                

    def checkMoves(self, row, col, m, grid, move_array):
        # given a position
        x = grid[row][col]
        # check if moves are valid
        move_count = []
        if row-1 >= 0:
            if grid[row-1][col+1] > x: #valid
                move_count.append(1 + move_array[row-1][col+1])
            else:
                move_count.append(0)
        if grid[row][col+1] > x:
            move_count.append(1 + move_array[row][col+1])
        else:
            move_count.append(0)

        if row+1 < m:
            if grid[row+1][col+1] > x: #valid
                move_count.append(1 + move_array[row+1][col+1])
            else:
                move_count.append(0)
        return max(move_count)



            


