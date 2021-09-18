class Solution:
    def canWin(self, s: str) -> bool:
        # creating nested helper function for recursively checking if win is possible
        def helper(self,s):
            # checking if the running of the particular function by the parameter is 
            # cached through memo, which is the point of storing it 
            if s in self.memo:
                return self.memo[s]
            # iterating through the "board" of +'s and -'s to see if a flip is possible
            for i in range(len(s)-1):
                # checking if the two elements are consecutive +'s before recursively 
                # searching simulating the gameboard given those changes
                if s[i] == '+' and s[i+1] == '+' and not helper(self, s[:i] + '--' + s[i+2:]):
                    # if it resolves recursively, in that another two ++'s cannot be switched,
                    # then the solution has been found
                    self.memo[s] = True
                    return True
            # if the end condition is not found, return false. note that these responses are
            # cached, to avoid going down bad trees more than once
            self.memo[s]=False
            return False
        # initializing a memoization, to map parameters to responses. very useful in python
        self.memo={}
        return helper(self, s)
    


chars = "++++---+---+++"
sol = Solution()
print(sol.canWin(chars))
print(chars)