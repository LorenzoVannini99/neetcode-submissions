"""

We know we have n as the number of nodes, so the max number of connected components is n.
Whatever algorithm we decide to have, after n iteration it should stop.

We have already look at NUMBER OF ISLAND problem and the solution should not be too far from that.

In this case something is connected when between two different node there is at least one edge.

Adjacency List provides the list of connected nodes from a node and it is quite natural to start from the nodes that has an indegree = 0.


For every edge [a, b], a and b are connected in both directions.

Build an Adjacency List:
    AL[a].append(b)
    AL[b].append(a)

Then start from a node and explore where I can go.

For example:

    0 — 1 — 2

Start from 0:
    can I go somewhere? Yes, I can go to 1.

Move to 1:
    can I go somewhere? Yes, I can go to 0 and 2.

0 was already visited, so skip it.
Go to 2.

From 2:
    I can go to 1, but 1 was already visited, so skip it.

At this point I have explored everything reachable from 0.
Therefore {0,1,2} is one connected component.

Then continue looking for a node that has not been visited.

Node 3 has not been visited:
    3 → 4

So {3,4} is another connected component.

Therefore:
    number of connected components = 2

The visited set is essential because otherwise I would keep going
back and forth:

    0 → 1 → 0 → 1 → 0 → ...

So the basic idea is:

    start from an unvisited node
        ↓
    explore every node I can reach
        ↓
    mark them as visited
        ↓
    one complete exploration = one connected component
        ↓
    find another unvisited node and repeat

"""

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        AL = { i : [] for i in range(n)}

        for a, b in edges:
            AL[a].append(b)
            AL[b].append(a)
        
        Visited= set()

        res = 0

        def dfs(node):

            if node in Visited:
                return 
            
            Visited.add(node)

            for nei in AL[node]:
                dfs(nei)
            
        for node in range(n):
            if node not in Visited:
                dfs(node)
                res += 1

        return res


        