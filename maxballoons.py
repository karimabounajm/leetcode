class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # return min([text.count('b'), text.count('a'), int(text.count('l')/2), int(text.count('o')/2), text.count('n')])
        return min([text.count('b'), text.count('a'), text.count('l')//2, text.count('o')//2, text.count('n')])


test = "balloonballoon"
sol = Solution()
print(sol.maxNumberOfBalloons(test))