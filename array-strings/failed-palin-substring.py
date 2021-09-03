from typing import List
import sys

class Solution:
    def isPalindrome(self, s: str, length: int, left_point: int, right_point: int, max: int) -> str:
        left = s[left_point:left_point-max-1:-1]
        right = s[right_point:right_point+max+1]
        if left != right:
            print(left, right)
            return max, False
        else:
            max += 1
        while left == right and right_point + max < length -1 and left_point - max > 0:
            if s[left_point-max] == s[right_point+max]:
                left += s[left_point-max]
                right += s[right_point+max]
                max += 1
            else:
                break
        return max, True
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if length == 0:
            return ""
        else:
            longest = 1
            ret = str(s[0])
        for i in range(length):
            if i - longest > 0 and i + longest < length and s[i - longest] == s[i + longest]:
                longest, f = self.isPalindrome(s, length, i, i, longest)
                if f:
                    ret = s[i-longest+1:i+longest]
                longest, f = self.isPalindrome(s, length, i, i+1, longest)
                if f:
                    ret = s[i-longest+1:i+longest]
        return ret


test = "xyzyjyzzzzzz"
sol = Solution()
print(sol.longestPalindrome(test))