"""
DFS Solution :

The problem states : " You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a."

Detect if at least one cycle exists.
You can solve this in multiple ways but simplest idea is to use an Adjacency List (AL)

AL is an hasmap where for each node you have the prerequisites. 
It is a sort of in-degree edges, which edges point at/towards me?

If I a course does not have pre req it points at nothing, so it is a leaf.
In order to do this use an AL.

If a node has empty AL[course] = [], is SAFE and return TRUE, meaning that the path is SAFE, the node is SAFE, it can be completed.

The subtlety is to use a vistied set, to properly backtrack the solution.

"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        AL = { i : [] for i in range(numCourses) }

        for c, p in prerequisites:
            AL[c].append(p)
        
        visited_path = set()

        def dfs(course) -> bool :

            # cycle has been detected
            if course in visited_path:
                return False

            # Safe course
            if AL[course] == []:
                return True

            visited_path.add(course)

            for p in AL[course]:
                if dfs(p) == False:
                    return False

            visited_path.remove(course)

            AL[course] = []

            return True


        for c in range(numCourses):
            if dfs(c) == False:
                return False

        return True
