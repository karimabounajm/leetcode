from collections import List, deque

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        wordSet = frozenset(wordDict)
        ans_ind, ans_str = [], []
        # methods of getting the maximum length
        # maxLength = max([len(x) for x in wordDict])
        maxLength = len(max(wordDict, key=len))
        # creating a deque of arrays, so array of arrays, with each array
        # element holding the index paths of the substrings 
        q = deque([[0]])
        while q:
            begin = q.popleft()
            index = begin[-1]
            for end in range(index+1, min(n+1, index+maxLength+1)):
                if s[index:end] in wordSet:
                    if end == n:
                        ans_ind.append(begin+[end])
                        continue
                    q.append(begin+[end])
        for sequence in ans_ind:
            prev, buffer = 0, []
            for i in range(1, len(sequence)):
                buffer.append(s[prev:sequence[i]])
                prev = sequence[i]
            ans_str.append(' '.join(buffer))
        return ans_str


# idea for improving efficiency: at the end of every for loop seach
# of all words begin to end, add all the complete paths to the full
# string found, or set it to false if no found are available. this 
# will allow for memoization of the problem, with the paths or lack
# thereof at every branch being saved, so that it doesn't need to be
# traversed multiple times

''' for this, I imagine simply maintaining a dictionary associating a 
given position with all the paths to a compelted string split of words,
being represented by an array of arrays, or an empty array showing that
there are no paths from this index to the complete string. this will all 
be saved at the end of every for loop, with a buffer array holding all of
the paths that are saved the exploration of the path '''
# for end in range(index+1, min(n+1, index+maxLength+1)):
#                 if s[index:end] in wordSet:
#                     if end == n:
#                         ans_ind.append(begin+[end])
#                         for i, val enumerate(ans_ind):
#                             dp[val] = ans_ind[-i-1:]
#                         continue
#                     q.append(begin+[end])