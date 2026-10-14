class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        book = {}
        for i in range(n):
            book[i] = []

        for i, j in edges:
            book[i].append(j)
            book[j].append(i)
        visited = {}
        def dfs(cur_edge, prev):
            if cur_edge not in visited:
                visited[cur_edge] = 1
            else:
                return False
            for nei in book[cur_edge]:
                if nei != prev:
                    if not dfs(nei, cur_edge):
                        return False
            return True
        
        return dfs(0, None) and len(visited) == n
        


