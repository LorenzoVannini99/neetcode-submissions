class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)

        for i in range(n):
            stones[i] = - stones[i]

        heapq.heapify(stones) # max heap
        while len(stones) > 1:
            
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if first < second :
                heapq.heappush(stones, first - second)

        
        if len(stones) == 1 :
            return - heapq.heappop(stones)
        else :
            return  0  
