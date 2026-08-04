class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1] * len(graph)
        queue = []
        
        for i in range(len(graph)):
            if color[i] == -1:
                queue.append(i)
                color[i] = 0
                while queue:
                    u = queue.pop(0)
                    for v in graph[u]:
                        if color[v] == -1:
                            color[v] = 1 - color[u]
                            queue.append(v)
                        if color[u] == color[v]:
                            return False
                            
        return True  
