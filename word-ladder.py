import string
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        # creating helper function for checking if a word
        # is one edit away from within dict
        def helper_word(word, wordSet, endSet, t, i):
            # extracting the left and right sides of the word
            # centered at the i'th character
            left = word[:i]
            right = word[i+1:]
            # iterating through all the characters in the alphabet
            for character in string.ascii_lowercase:
                n = left + character + right
                if n in wordSet:
                    if n in endSet:
                        return transformations
                    else:
                        t.add(n)
            return None
            
        # using set to hold words, removing duplicates
        wordSet = set(wordList)
        # base case, checking if the word exists 
        if endWord not in wordSet:
            return 0
        # creating dictionaries for two ended BFS
        beginSet = {beginWord}
        endSet = {endWord}
        transformations = 1
        while beginSet:
            # there is no need to check words that are currently a part of
            # or have been checked by the beginSet dictionary
            wordSet -= beginSet
            transformations += 1
            t = set()
            for word in beginSet:
                for i in range(len(word)):
                    if helper_word(word, wordSet, endSet, t, i):
                        return transformations
            beginSet = t
            if len(beginSet) > len(endSet):
                endSet, beginSet = beginSet, endSet
        return 0