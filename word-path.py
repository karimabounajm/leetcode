class Solution:
    # BFS
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # put beginWord into wordList
        wordList.append(beginWord)
        
        # build a hash map to mapping patternn to words
        d = collections.defaultdict(set)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                d[pattern].add(word)

        # use a set to record visited words
        visited = set([beginWord])
        
        # use the queue to do BFS
        queue = collections.deque([beginWord])
        
        # use a dict, which allSeq[word] is a sequence end with word
        allSeq = collections.defaultdict(list)
        allSeq[beginWord].append([beginWord])
        
        while queue:
            new_queue = collections.deque()
            
            curVisited = set()
            while queue:
                curWord = queue.popleft()
                
                if curWord == endWord:
                    return allSeq[curWord]
        
                for i in range(len(curWord)):
                    pattern = curWord[:i] + '*' + curWord[i+1:]

                    for neighbor in d[pattern]:
                        if neighbor in visited or neighbor == pattern:
                            continue
                               
                        for l in allSeq[curWord]:
                            allSeq[neighbor].append(l + [neighbor])

                        if neighbor not in curVisited:
                            new_queue.append(neighbor)
                            curVisited.add(neighbor)
                        
            for v in curVisited:
                visited.add(v)
            
            queue = new_queue
        
        return []