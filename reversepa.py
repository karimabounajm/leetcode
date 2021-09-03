class Solution:
    def reverseParentheses(self, s: str) -> str:
        st = []
    
        for i in range(len(s)):
            if (s[i] == '('):
                st.append(i)
            elif (s[i] == ')'):
                temp = s[st[-1]:i + 1]
                s = s[:st[-1]] + temp[::-1] + \
                    s[i + 1:]
        final = ""
        for i in range(len(s)):
            if (s[i] != ')' and s[i] != '('):
                final += (s[i])
        return final

test = "n(ev(t)((()lfevf))yd)cb()"
sol = Solution()
print(sol.reverseParentheses(test))