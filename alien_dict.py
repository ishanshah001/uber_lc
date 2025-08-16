class Solution:
    def alienOrder(self, words):
        # Build adjacency list for all unique characters
        adj = {ch: set() for word in words for ch in word}

        # Build graph from word ordering
        for w1, w2 in zip(words, words[1:]):
            min_len = min(len(w1), len(w2))
            if w1[:min_len] == w2[:min_len] and len(w1) > len(w2):
                return ""  # invalid ordering
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    adj[c1].add(c2)
                    break

        visited = {}  # char -> bool (True = in current DFS path)
        order = []

        def dfs(ch):
            if ch in visited:
                return visited[ch]  # True means cycle found
            visited[ch] = True
            for nei in adj[ch]:
                if dfs(nei):
                    return True
            visited[ch] = False
            order.append(ch)

        # DFS for all characters
        for ch in adj:
            if dfs(ch):
                return ""  # cycle found → invalid

        return "".join(reversed(order))
