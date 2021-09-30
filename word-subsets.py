from typing import List
from collections import Counter, defaultdict

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # creating dictionary for maximum number of characters required
        # all in all, across all of the substring requirements in word2
        dic = defaultdict(int)
        for i in words2:
            # finding the count of all characters in the substring
            tempdic = Counter(i)
            # updating the dictionary with the maximum count 
            for j, val in tempdic.items():
                dic[j] = max(dic[j], val)
        # initializing answer array
        ans = []
        # iterating through the words in word1 to check if they meet 
        # the character requirements in word2
        for i in words1:
            # creating boolean value to see whether or not the word
            # should be added, set to False if the requirement of 
            # a character is not met by a word
            add = True
            # using the items method, however using keys and have
            # hashing return the val is also an option, save memory
            for j, val in dic.items():
                if i.count(j) < val:
                    add = False
                    break
            if add:
                ans.append(i)
        return ans
