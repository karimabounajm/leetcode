

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        if length < 2:
            return length
        # creatina a hash table for dynamic sliding
        dictionary = {}
        # initializing the values
        ans = left = 0
        # iterating throught the provided string, tracking the 
        # character and its respective index
        for right, c in enumerate(s):
            # checking if the character is in the dictionary,
            # which would mean that the respective character in 
            # the string that the array is going through would
            # form a string that is at the longest, given what we
            # already know, between itself and the left pointer
            if c in dictionary:
                # if left is not in the dictionary than the longest
                # string that can be formed is from the beginning to
                # the current character in the outer iteration
                left = max(left, dictionary[c])
            # updating the answer if a longer substring has been found
            ans = max(ans, right - left + 1)
            dictionary[c] = right + 1
            print(left, right)
        return ans


test = "helllllooooooooo there"
sol = Solution()
print(sol.lengthOfLongestSubstring(test))
