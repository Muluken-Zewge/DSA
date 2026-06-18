'''we assume a tree rooted at node 0, and make sure every node points to it's parent so that any node can reach to node 0. if there are nodes not pointing to their parents, we reverse them. since it's a tree, there is only one way b/n any two nodes, so the reversal is automatically minimum. we either reverse or not, there is no other path that can be compared for optimality.
'''
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # form a graph
        graph = defaultdict(list)
        for u,v in connections:
            graph[u].append((v,True))
            graph[v].append((u,False))
        
        # define a dfs function to traverse over the graph
        visited = set()
        def dfs(node):
            visited.add(node)
            reversals = 0

            for neighbor, is_forward in graph[node]: # is_forward == away from parent
                if neighbor not in visited:
                    if is_forward:
                        reversals += 1
                    reversals += dfs(neighbor)
            
            return reversals
        
        return dfs(0)
