
from typing import List

class Solution:
    def findPermutation(self, s: str) -> List[int]:
        # getting helper variables, holding consecutive symbols
        length, i = len(s), 0
        ans = []
        while i < length:
            # counting the number of consecutive symbols 
            symbol, index = s[i], i
            while i < length-1 and s[i] == s[i+1]:
                i += 1
            # incrementing the index and the iterator for adding 
            # to the array of answers
            index += 1
            i += 1
            # adding the symbols sequentially if I
            if symbol == 'I':
                i += 1
                ans += list(range(index, i))
            # adding the symbols in reverse if D
            else:  
                i += 1
                ans += list(range(i+1, index-1, -1))
        # returning ans
        return ans 

nums = "IIDDIIDDIDI"
sol = Solution()
print(sol.findPermutation(nums))
print(nums)