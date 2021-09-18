class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        def helper(pattern, string, char_map={}, substr_map={}):
            # if all the chars in the pattern have been mapped but result
            # has all chars used and string still having unmapped parts
            if not pattern and string:
                return False
            # if all the characters in pattern have been mapped and the
            # string itself is also fully mapped, end condition
            if not pattern and not string:
                return True
            # iterating through the current string and checking all the
            # mapping of characters to subsets of the string
            for length in range(1, len(string) - len(pattern) + 1 + 1):
                # extracting the next pattern character and a substring of 
                # remaning string to assign the character to
                p, s = pattern[0], string[:length]
                # checking of the character is already mapped to a substring
                # and if not, mapping character to substring and substring to
                # character, as well as backtracing by continuing the process
                # of assigning substrings to characters until one in which the
                # passing base case is found
                if p not in char_map and s not in substr_map:
                    char_map[p] = s
                    substr_map[s] = p
                    # using recursion to backtrace, continuing the current 
                    # configuration of characters to sub strings to see if 
                    # a solution from this pattern will result in all the 
                    # characters being mapped to substrings and the original
                    # string having all its parts mapped bijectively 
                    if helper(pattern[1:], string[length:], char_map, substr_map):
                        return char_map, substr_map, True
                    # removes the assignment of character to substring and 
                    # vice versa, in case the backtracing in this branch failed
                    del char_map[p]
                    del substr_map[s]
                # this is in case the character has already been mapped to a 
                # substring and the substring is correctly mapped, in which 
                # case continue with the algorithm starting with a new character
                # in the pattern, success in mapping another character so far
                elif p in char_map and char_map[p] == s :
                    if helper(pattern[1:], string[length:], char_map, substr_map):
                        return char_map, substr_map, True
                # the loop continues, to accommodate for the cases in which the 
                # character is already mapped to a substring however the current
                # in the loop is not matching the one the character is mapepd to.
                # allowing the loop to continue running allows for the potential 
                # mapping of the character with a proper substring
            return False
        
        return bool(helper(pattern, s))

chars = "aba"
word = "reddbluered"
sol = Solution()
print(sol.wordPatternMatch(chars, word))
print(chars, word)