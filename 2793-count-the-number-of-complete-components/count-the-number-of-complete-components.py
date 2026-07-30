class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        # def dfs(node):
        #     if node in visited:
        #         return 0,0

        #     visited.add(node)

        #     nodes = 1
        #     edge_count = len(graph[node])
        #     for child in graph[node]:
        #         child_nodes, child_edges = dfs(child)
        #         nodes += child_nodes
        #         edge_count += child_edges
            
        #     return nodes,edge_count

        # ans = 0
        # for node in range(n):
        #     if node not in visited:
        #         nodes, edges = dfs(node)
        #         edges //= 2 # edges were counted twice
        #         if edges == nodes*(nodes - 1)//2:
        #             ans += 1
        
        # return ans
        print(graph)
        ans = 0
        for i in range(n):
            if i in visited:
                continue

            queue = deque([i])
            visited.add(i)
            nodes, edge_count = 0, 0

            while queue:
                node = queue.popleft()
                nodes += 1
                edge_count += len(graph[node])

                for child in graph[node]:
                    if child not in visited:
                        queue.append(child)
                        visited.add(child)
            
            if edge_count//2 == nodes*(nodes - 1)//2:
                ans += 1
        
        return ans
            
        
