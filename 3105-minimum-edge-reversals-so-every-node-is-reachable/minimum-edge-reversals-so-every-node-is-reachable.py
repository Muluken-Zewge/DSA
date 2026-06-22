'''we use rerooting dp. we run dfs once to get the min edge reversal needed to reach every node by rooting the tree at node 0. and we use that info in our second dfs to get the answer using dp. the core idea is when we travrse from parent to child in our second dfs, we reroot the tree at the child node. so that we only check the r/ship b/n the parent and child to get the answer for child using the dp value of the parent.
'''
class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        # build graph(we want every parent pointing to their children)
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append((v,False)) #(child,needs_reversal)
            graph[v].append((u,True))
        
        ans = [0] * n

        # first dfs: find ans[0]
        def dfs(node,parent):
            for neighbour, needs_reversal in graph[node]:
                if neighbour == parent:
                    continue  
                if needs_reversal:
                    ans[0] += 1
                dfs(neighbour,node)
        
        dfs(0,-1)

        # second dfs: rerooting dp
        def reroot(node,parent):
            for neighbour,was_reversed in graph[node]:
                if neighbour == parent:
                    continue

                # originally reversed,but for the child to be the root, it's ok. so we decrement what we previosuly incremented.
                if was_reversed:
                    ans[neighbour] = ans[node] - 1
                else:
                    ans[neighbour] = ans[node] + 1

                reroot(neighbour,node)
        
        reroot(0,-1)

        return ans