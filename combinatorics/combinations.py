
from typing import List

# efficient solution to creating an array of combinations, note however
# that there is a method in python that already does this:
'''
from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return combinations(range(1,n+1),k)
'''


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def helper(n, k, next_min, comb):
            if len(comb) == k:
                self.ans.append(comb)
                return
            for i in range(next_min, n+1):
                # checking if inserting the the next index will result in
                # a combination that will require a number that exceed n,
                # and if so breaking to avoid going down bad branch
                if n - i + 1 < k - len(comb):
                    break
                # i+1 inserted because i represents the new maximum
                # and newest value inserted into the current combination
                # is added to the comb
                helper(n, k, i+1, comb+[i])

        self.ans = []
        helper(n, k, 1, [])
        return self.ans


sol = Solution()
print(sol.combine(8, 5))
# print(chars)
