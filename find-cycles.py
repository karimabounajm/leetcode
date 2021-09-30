from collections import defaultdict
from typing import List
class Solution(object):
    # simple strategy, form an adjacency list and traverse all of 
    # the edges, findingi out
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # using defaultdict for graph due to its ability to 
        # form elements based on unused keys as they are called
        # even if they do not exist yet
        courseDict = defaultdict(list)
        # creating an adjacency list for all the edges in the
        # graph connecting courses, directed edges
        for relation in prerequisites:
            courseDict[relation[1]].append(relation[0])
        # initializing arrays that hold nodes that are checked
        # and that are in the current path
        checked, path = [False] * numCourses, [False] * numCourses
        # performing a depth first search, with the driver method
        # starting a search at every vertex of the graph however
        # allowing for the function to be ended early if a cycle
        for currCourse in range(numCourses):
            if self.isCyclic(currCourse, courseDict, checked, path):
                return False
        return True
    def isCyclic(self, currCourse, courseDict, checked, path):
        # checking base cases, where the first is if this node has already
        # been checked, and the second being if this node has already been
        # visited in the current path, meaning a cycle exists
        if checked[currCourse]:
            return False
        if path[currCourse]:
            return True
        # marking that the current node on the path has been visited
        path[currCourse] = True
        # visiting all the outward edges from the current node, as 
        # stored in the adjacency list of the graph
        for child in courseDict[currCourse]:
            # checking if the child node itself will lead to a cycle, 
            # and if so returning True, ending the algorithm
            if self.isCyclic(child, courseDict, checked, path):
                return True
        # removing the marking from the global path array that shows
        # that the current node has been visited, backtracing, and
        # also marking that the current node has been checked
        path[currCourse] = False
        checked[currCourse] = True
        # returning False, as no cycle was found
        return False



from collections import defaultdict
from typing import List
class Solution(object):
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseDict = defaultdict(list)
        for relation in prerequisites:
            courseDict[relation[1]].append(relation[0])
        checked, path = [False] * numCourses, [False] * numCourses
        for currCourse in range(numCourses):
            if self.isCyclic(currCourse, courseDict, checked, path):
                return False
        return True
    def isCyclic(self, currCourse, courseDict, checked, path):
        if checked[currCourse]:
            return False
        if path[currCourse]:
            return True
        path[currCourse] = True
        for child in courseDict[currCourse]:
            if self.isCyclic(child, courseDict, checked, path):
                return True
        path[currCourse] = False
        checked[currCourse] = True
        return False

