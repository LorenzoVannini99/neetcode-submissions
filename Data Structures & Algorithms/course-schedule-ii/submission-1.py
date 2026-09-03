class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        AL = {i : [] for i in range(numCourses)}
        indegree = [0] * numCourses
        res = []
        processed = 0
        q = deque()

        for c, p in prerequisites:
            AL[p].append(c)
            indegree[c] += 1
        
        for c in range(len(indegree)):
            if indegree[c] == 0:
                q.append(c)
                res.append(c)

        if len(q) == 0:
            return []

        while q:

            node = q.popleft()
            processed += 1
            
            for nei in AL[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
                    res.append(nei)


        if processed == numCourses:
            return res 
        else:
            return []   


        