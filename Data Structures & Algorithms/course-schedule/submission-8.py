"""
Topological Sort (Kahn's Algorithm) :

Idea : you do not need to find a cycle like classical DFS style.
Use graph math

In degree is the number of edges pointing toward a node.
In degree(node) = how many pointing arrows I have.

In this case a node that has an in degree = 5 it means that it requires to take 5 courses.
If a node is safe has an in degree = 0

If you really have an in depth thinking is not quite different from Adjacency List solution, using DFS.
How did we make sure that a node is safe? --> AL[node] = [].
That was our memoization techinique, avoiding really high time complexity.

What is the safe condition? --> no pre req == in degree = 0.

# Intuition
start from the safe node and remove them ( with their edges ) from the other nodes. 
Process only 0 in degree nodes. 
Safety must propagate a number of numCourses times.

# This is Kahn's Algorithm. 
- find all possible in degree = 0 node. If there is no in degree node = 0 return False. There must be a cyle because each node requires at least another node
- If you find one append it to deque
- If a node is connected to a 0 degree node ( a.k.a safe node ) we can reduce one edge, we are indeed cutting that edge. The safe edge is cut and other nodes have to be processed.
- If the number of processed nodes == nodes --> return True else False.

"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        if not prerequisites:
            return True

        processed = 0

        # Adjacency List
        AL = {i : [] for i in range(numCourses)}

        # create a list where the index is the node course, 
        # and the value is how many in degree connections it has
        indegree = [0] * numCourses

        for c, p in prerequisites:
            AL[p].append(c)
            indegree[c] += 1
        
        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append( i )


        while q:
            node = q.popleft()
            processed += 1

            for nei in AL[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)


        return processed == numCourses



        