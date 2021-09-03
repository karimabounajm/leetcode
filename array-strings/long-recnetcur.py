

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        if length < 2:
          return length
        # creatina a hash table for dynamic sliding
        hash_table = {}
        # initializing the values 
        ans = left = 0
        for right, c in enumerate(s):
          if c in hash_table:
            left = max(left, hash_table[c])
          ans = max(ans, right - left + 1)
          hash_table[c] = right + 1
        return ans
          
        

test = "helllllooooooooo there"
sol = Solution()
print(sol.lengthOfLongestSubstring(test))