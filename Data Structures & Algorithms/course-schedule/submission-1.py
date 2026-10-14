class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        book = {}
        for i in range(numCourses):
            book[i] = []

        for i , j in prerequisites:
            book[i].append(j)

        visited = set()
        def dfs(course):
            if book[course] == []:
                return True
            if course in visited:
                return False

            visited.add(course)
            for pre in book[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            book[course] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True