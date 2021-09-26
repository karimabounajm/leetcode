
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # immediate check to see if the board and word exists
        if not board or not word:
            return False
        # defining operations for readability
        operations = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        length = len(word)
        # defining a helper function to perform a depth first search
        # from a given coordinate (character in board); note, passing
        # the variables by reference to nested function for speed
        def dfs(board, word, i, j, substr, index, length, operators):
            # checking if the right length has been found, given that 
            # all characters in substring are verified as being part
            # of the word being searched for (ie word is found)
            if index == length:
                return True
            # iterating through the operations and checking to see 
            # whether or not the branch should be further explored
            for x, y in operations:
                if (i + x) >= 0 and (i + x) < len(board) and (j + y) >= 0 and (j + y) < len(board[0]) and board[i + x][j + y] == word[index] and board[i + x][j + y] != '#':
                    # add symbol to indicate that the character has been visited, so that 
                    # it is not visited again in this branch
                    board[i + x][j + y] = '#'
                    # call is made to continue searching through the branch 
                    if dfs(board, word, i + x, j + y, substr + word[index], index + 1, length, operators):
                        return True
                    # backtracing to allow for the exploration of visited character in 
                    # other branches, as its position in the word determines its use and
                    # must be explorable by other values
                    board[i + x][j + y] = word[index]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    board[i][j] = '#'
                    if dfs(board, word, i, j, word[0], 1, length, operations):
                        return True
                    board[i][j] = word[0]
        return False
        

boards = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
words = "ABCCED"

sol = Solution()
print(sol.exist(boards, words))
# print(chars)