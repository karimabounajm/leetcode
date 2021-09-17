from typing import List
from collections import deque

class Solution:
    # finding all the combinations of the following list
    def letterCombinationsIterative(self, digits: str) -> List[str]:
      # checking if the string is empty
      if digits == "":
          return []
      # creating a dictionary associating number with its possible letters
      letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                 "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
      # initialzing the deque with the possible characters of the first number in the digits
      q = deque(letters[digits[0]])
      # using more efficient for loop that ends when all the elements in the
      # deque are popped, for when len of them are removed
      for i in range(1,len(digits)):
          s = len(q)
          while s:
              out = q.popleft()
              for j in letters[digits[i]]:
                  q.append(out + j)
              s -= 1
      return q
    def letterCombinations(self, digits: str) -> List[str]:
      # checking if the string is empty
      if len(digits) == 0: 
        return []
      # creating a dictionary associating number with its possible letters
      letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                 "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
      # defining submethod for backtracking (which is by definition recursive)
      def backtrack(index, path, length):
          # if the current index is equal to the length of the string-1, then a combination
          # has been successfully created
          if index == length:
              "".join(path)
              combinations.append("".join(path))
              return
          # extracting the string of possible letters for number from dictionary
          possible_letters = letters[digits[index]]
          # iterating over the characters, and adding them to the current string
          for letter in possible_letters:
              # adding the letter to the string as a discrete character, so it can be popped
              path.append(letter)
              # recursively calling backtrack while incrementing index by 1, moving forward
              backtrack(index + 1, path, length)
              # popping the last element of string, so that the array that is passed by reference
              # of the current string is ready for the next iteration/recursive call with new char
              path.pop()
      # getting the length of the input array for parameter, use to check if new word is complete
      length = len(digits)
      # initializing the combinations array that will be modified, as it is passed by reference
      combinations = []
      backtrack(0, [], length)
      return combinations