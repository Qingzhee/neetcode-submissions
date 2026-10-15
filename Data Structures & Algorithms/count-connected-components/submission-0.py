class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        links = {i: [] for i in range(n)}

        for i, j in edges:
            links[i].append(j)
            links[j].append(i)

        seen = set()
        counter = 0
        def dfs(edge):
            if edge in seen:
                return 
            seen.add(edge)
            for nei in links[edge]:
                dfs(nei)

        for i in range(n):
            if i not in seen:
                counter += 1
                dfs(i)

        return counter