from collections import defaultdict, deque
class Solution:

    def findOrder(self, numCourses, prerequisites):
        # creating an adjacency list and tracking the indegree values
        # of the vertices in the graph, for finding roots for bfs
        adj_list = defaultdict(list)
        indegree = {}
        for dest, src in prerequisites:
            adj_list[src].append(dest)
            indegree[dest] = indegree.get(dest, 0) + 1
        # creating a deque that contains all of the vertices that are
        # tracked as having no incoming edges, meaning they are roots, 
        # essentially forming the vertices starting the bfs
        queue = deque([k for k in range(numCourses) if k not in indegree])
        # defining nested helper function for performing dfs
        def helper_dfs(queue, ans, adj_list, indegree):
            while queue:
                vertex = queue.popleft()
                ans.append(vertex)
                if vertex in adj_list:
                    for neighbor in adj_list[vertex]:
                        indegree[neighbor] -= 1
                        if indegree[neighbor] == 0:
                            queue.append(neighbor)
            return ans
        # calling the nested helper function
        ans = helper_dfs(queue, [], adj_list, indegree)
        return ans if len(ans) == numCourses else []