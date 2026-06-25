class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = [-x for x in stones]
        heapq.heapify(pq)

        while len(pq) > 1:
            heaviest1 = -heapq.heappop(pq)
            heaviest2 = -heapq.heappop(pq)

            if heaviest1 < heaviest2:
                new_stone = heaviest2 - heaviest1
                heapq.heappush(pq, -new_stone)
            elif heaviest1 > heaviest2:
                new_stone = heaviest1 - heaviest2
                heapq.heappush(pq, -new_stone)
                
        if not pq:
            return 0

        return -pq[0]
