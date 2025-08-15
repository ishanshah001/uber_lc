from collections import defaultdict

class Solution:
    def collectTheCoins(self, coins, edges):
        if not edges:
            return 0

        # Build adjacency list
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        # Remove leaves with no coins
        def trim_coinless_leaves():
            leaves = [node for node in graph if len(graph[node]) == 1]
            for leaf in leaves:
                while leaf in graph and len(graph[leaf]) == 1 and coins[leaf] == 0:
                    parent = graph[leaf].pop()
                    del graph[leaf]
                    if parent in graph:
                        graph[parent].remove(leaf)
                    leaf = parent

        trim_coinless_leaves()

        # Remove leaves twice
        for _ in range(2):
            leaves = [node for node in graph if len(graph[node]) == 1]
            for leaf in leaves:
                if leaf not in graph:
                    continue
                parent = graph[leaf].pop()
                del graph[leaf]
                if parent in graph:
                    graph[parent].remove(leaf)
                if len(graph) < 2:
                    return 0

        # Remaining edges = (nodes - 1) in a tree, each counted twice
        return 2 * (len(graph) - 1)
