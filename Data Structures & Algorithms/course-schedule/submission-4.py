"""
DFS solution

I could not solve this problem by myself, I spent too much time on it so you should not.

The graph is valid if no cycle is detected. 

By definition a cycle is a path where you stumble upon at least twice a node in that path.
Use a visited set to store visited nodes in a path, if at least one cycle is detected return False.

There is one small catch, the graph can be disconnected : A -> C and B -> C.
Visting C twice does not mean a cycle is detected. 
The subtlety is to make sure we remove a course from the vistited set after completion.

The core idea is to create an adjacency list that maps course in prereq, if a course has no prereq is SAFE.
When a course does not need another course it cannot create a cycle, so simply put a [] and return True.
Whenever dfs finds a safe course it will see [] and will return TRUE. It is  a good way to do memoization, in O(1) I can immediately say : " I have already visited this, return True".
As I see it, this implementation is an elegant way of prune the tree.
A solution exploiting 2 different sets (visited and visiting) can be used. 

It seems like a small implementation detail but without the [], the memoization part, the TC can explode, think about it, if you return true only if no cycle is detected you look in every possible path.

Example :

2 → 1 → 0

AdjList = {
    0: [],
    1: [0],
    2: [1]
}

Inside dfs(0) --> 0 ∉ visited --> nothing happens
if AdjList[course] == [] --> this is TRUE
dfs(0) → True

Inside dfs(1) --> 1 ∉ visited --> nothing happens
if AdjList[1] == [] --> False
now visited = {1}

for p in AdjList[1] --> just run dfs(0) --> True

This loop has finished so remove visited

Same thing for dfs(2) sicne dfs(1) returns TRUE
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        AdjList = { i : [] for i in range(numCourses) }
        
        for p, c in prerequisites:
            AdjList[c].append(p)

        visited = set()

        def dfs( course ):
            
            # Is it valid?
            if course in visited:
                return False
            
            # memoization : have i already visited this?
            if AdjList[course] == []:
                return True
        
            visited.add(course)

            # Visit all prereq with dfs
            for p in AdjList[course]:
                if dfs( p ) == False:
                    return False
            
            # If nothing has returned False i can do this course
            # This is SAFE, remove from current path and explore other courses
            visited.remove(course)

            AdjList[course] = []
            
            return True

        for courses in range(numCourses):
            if not dfs(courses):
                return False

        return True





        
        