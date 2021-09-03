from typing import List
import sys

class Solution:
    def depthSearch(self, ans: List, curString: List, s:str, left:int, right:int) -> bool:
        if left > len(s) or right > len(s):
            return False
        string = s[left:right]
        if string == string[::-1]:
            ans.append(string)
            self.depthSearch(ans, s, left, right+1)
            self.depthSearch(ans, s, left+1, right+1)
            return True
        else:
            self.depthSearch(ans, s, left, right+1)
            return False
    def partition(self, s: str) -> List[List[str]]:
        ans = list()
        self.depthSearch(ans, s, 0, 1)
        return ans
        
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def isPalindrome(start_ind, end_ind):
            while start_ind <= end_ind:
                if s[start_ind] != s[end_ind]: return False
                start_ind += 1
                end_ind -=1
            return True
        
        def dfs(start_ind, path):
            if start_ind >= len(s): self.res.append(path)
                
            for l in range(len(s) - start_ind):
                if isPalindrome(start_ind, start_ind + l):
                    dfs(start_ind + l + 1, path + [s[start_ind:start_ind + l + 1]] )
        
        self.res = []
        dfs(0,[])
        return self.res

test = "aab"
sol = Solution()
print(sol.partition(test))