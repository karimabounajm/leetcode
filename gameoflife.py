
from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                # checking and saving if the original cell is alive or dead
                is_live = board[i][j] > 0
                # note that the number of lives in this instance, which is adjusted
                # by 1 because of the positive-negative encoding of living-dead in 
                # cells, contains the number of living values in the cells in the 
                # row above the current cell and the cell to its left
                lives = abs(board[i][j]) - is_live
                # iterating over the row beneath the current cell and the next
                # cell on the board, which will check for the number of lives 
                # on the board that aren't already accounted for previously in 
                # the algorithm; 
                for r, c in (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1):
                    if r < m and 0 <= c < n:
                        # incrementing the number of lives if the cell is alive
                        lives += board[r][c] > 0
                        # incrementing the adjacent cell if the current cell is
                        # originally alive (if the value is positive), or decrementing
                        # the adjacent cell if it itself is a negative value and thus
                        # originally dead, and is represented negatively
                        board[r][c] += is_live if board[r][c] > 0 else -is_live
                # with the number of lives in all 8 adjacent cells accounted for, 
                # 4 previously in the algorithm in iterations of the for loop above,
                # the current board will be determined as alive if there are 3 
                # adjacent living cells or if there are two adjacent living cells
                # and the current cell is originally alive
                board[i][j] = int(lives == 3 or (is_live and lives == 2))


'''
Lol this is way more complex than just using the signs - and it took me a while to puzzle out.
It's able to complete the problem in 1 pass by updating the neighbors that the main loop has yet to visit (i.e. the one on its right and the 3 below it).
This allows it to safely set the cell to its final value before moving onto the next cell, and to assume that when the main loop reaches a cell, it already 
contains a sum of the neighbors that were already visited - but this sum is encoded by the original sign of the cell. So sums that are greater than 0 are the 
cell's original value of 1 plus the number of previously visited neighbors that were 1, while sums that are 0 or less are the cell's original vale of 0 minus 
1 for every previously visited neighbor that was 1.
The only other confusing part is that in lives = abs(board[i][j]) - is_live, the - is_live is used to eliminate the cell's own original value from the encoded neighbor sum.
'''