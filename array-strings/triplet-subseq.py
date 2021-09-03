from typing import List
import sys

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        lower = middle = upper = sys.maxsize
        for n in nums:
            if n <= lower:
                lower = n
            elif n <= middle:
                middle = n
            elif n <= upper:
                return True
        return False


test = [-1,0,1,0]
sol = Solution()
print(sol.increasingTriplet([2,7,-2, 3]))