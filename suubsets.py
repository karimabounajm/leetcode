
from typing import List
class Solution:
    def subsets(self, nums: List[int]):
        result = [[]]
        for num in nums:
            length = len(result)
            for i in range(length):
                result.append(result[i] + [num])
        return result
    # alternative pythonic solution
    def subsetsPythonic(self, nums: List[int]):
        ret = [[]]
        for n in nums:
            # iterating through all of the current values in 
            # return, and appending to return what would be 
            # concatenated versions of the current values with
            # the value that is currently inside of the set
            ret += [item + [n] for item in ret]
        return ret