from collections import defaultdict

class Solution:
    def calcEquation(self, equations, values, queries):
        # Build graph
        graph = defaultdict(dict)
        for (u, v), val in zip(equations, values):
            graph[u][v] = val
            graph[v][u] = 1 / val

        # DFS search
        def dfs(u, v, visited):
            if u not in graph or v not in graph:
                return -1.0
            if u == v:
                return 1.0
            visited.add(u)
            for nei, w in graph[u].items():
                if nei not in visited:
                    res = dfs(nei, v, visited)
                    if res != -1.0:
                        return w * res
            return -1.0

        # Answer queries
        return [dfs(a, b, set()) for a, b in queries]