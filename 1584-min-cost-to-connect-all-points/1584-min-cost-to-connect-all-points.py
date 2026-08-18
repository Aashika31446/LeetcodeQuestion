import heapq

class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        ans = 0
        n = len(points)
        cost = [float('inf')] * n
        visited = [0] * n
        pq = [(0, 0)] 
        cost[0] = 0
        
        while pq:
            c, u = heapq.heappop(pq)
            if visited[u]:
                continue
            ans += c
            visited[u] = 1
            
            for v in range(n):
                if not visited[v]:
                    dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    if dist < cost[v]:
                        cost[v] = dist
                        heapq.heappush(pq, (cost[v], v))
                        
        return ans
