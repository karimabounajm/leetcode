
class Solution:
    def countSubstringsManacher(self, s: str) -> int:
        length, count, combo = len(s), 0, 1
        for i in range(length):
            if combo == 1:
                count += 1
                j, k = 1, i
                if i+j < length and s[i] == s[i+j]:
                    while i+j < length and s[i] == s[i+j]:
                        combo += 1
                        j += 1
                    count += int((combo/2) * (1+combo) -1)
                    k = i+j-1
                    j = 1
                while -1 < i-j and k+j < length and s[i-j] == s[k+j]:
                    count += 1
                    j += 1
            else:
                combo -= 1
        return count
    def countSubstrings(self, s: str) -> int:
        # find all palindromes starting at centerd
        def countPalinCenter(current, low, high):
            ans = 0
            # counting the number of palindromes that can be formed
            while low >= 0 and high < len(s) and s[low] == s[high]:
                ans += 1
                low -= 1
                high += 1
            return ans
        # finding all the palindromes by treating each character and 
        # pair of characters as the center of a palindrome
        ans = 0
        for i in range(len(s)):
            # calling helper for odd palindromes
            ans += countPalinCenter(s, i, i)
            # calling helper for even palindromes, if they form a valid palindrome
            if i < len(s)-1 and s[i] == s[i+1]:
                ans += countPalinCenter(s, i, i+1)
            # ans += countPalinCenter(s, i, i+1)
        return ans
