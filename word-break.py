class Solution:
    def wordBreakIterative(self, s: str, wordDict: List[str]) -> bool:
        # creating an array of values that indicate if the current 
        # position has been explored, effectively stopping the searching
        # down paths that cannot yield a solution
        n = len(s)
        dp = [False for _ in range(n)]
        # frozenset used for hashable values, can search for words
        # by using the python "in" opreator in O(1) time
        wordSet = frozenset(wordDict)
        # finding the maximum length of a word in the provided dict,
        # something that can be used to limit how far down a branch
        # the algorithm will explore before ending because no word 
        # is possible, as none exist with the length required
        maxLength = max([len(x) for x in wordDict])
        # initializing an array that holds the values of the 
        q = deque([0])
        while q:
            begin = q.popleft()
            if dp[begin]:
                # if this value is true then the algorithm has already
                # explored the branch starting at this index
                continue
            # setting the element at this index to true to indicate
            # that the branch is about to be explored
            dp[begin] = True
            # exploring the branch and trying to find a word, with the 
            # number of characters being limited by the end of the string
            # provided as input and by the maximum lengthed word in the
            # dictionary provided
            for end in range(begin+1, min(n+1, begin+maxLength+1)):
                if s[begin:end] in wordSet:
                    if end == n:
                        return True
                    q.append(end)
        return False
    ''' conventional recursive depth first approach '''
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # the lru_cache decorater is for memoization, with any
        # repetitions of the parameters into the depth_first function
        # having their values and functionality saved; 
        @lru_cache
        # creating a function that appends all of the indices at
        # which a slice of the remaining string matches a word in
        # the word dictionary provided
        def depth_first(start):
            # iterating over all of the combinations in the 
            # slice of the string remaining in this branch
            for i in range(start, len(s)+1):
                # checking if this subslice is a word in the 
                # words dictionary
                if s[start:i] in word_set:
                    # if this new word ends at the end of the 
                    # string provided, then answer is found
                    if i == len(s):
                        return True
                    comb.append(i)
        # base cases validating input
        if not s or not wordDict:
            return False
        # initializing words into hashable dictionary and 
        # creating a deque for breadth first search
        word_set = frozenset(wordDict)
        comb = deque([0])
        # checking for combinations while there are 
        while comb:
            start_index = comb.pop()
            if depth_first(start_index):
                return True
        return False
