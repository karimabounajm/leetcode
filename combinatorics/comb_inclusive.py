from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
      # creating a recursive helper function
      def backtracing(current, array, length):
        # base case 
        if length == k:
          if current == n and array not in ans:
            ans.append(list(array))
          return
        for j in range(array[length-1]+1, 10):
          if current + j <= n:
            array.append(j)
            backtracing(current+j, array, length+1)
            array.pop()
          else:
            break
      ans = []
      for i in range(1, 10):
        backtracing(i, [i], 1)      
      return ans
        
        