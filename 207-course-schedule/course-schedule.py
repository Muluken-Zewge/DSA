class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # khan's algorithm
        n = numCourses
        graph = defaultdict(list)
        indegree = [0] * n
        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        queue = deque()
        for node in range(n):
            if indegree[node] == 0:
                queue.append(node)

        res = [] # answer array that stores the order
        while queue:
            node = queue.popleft()
            res.append(node)

            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        return len(res) == n