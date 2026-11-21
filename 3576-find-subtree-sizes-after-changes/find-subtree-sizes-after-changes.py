class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)
            
        new_parent = list(parent)
        last_seen = {}
        
        # Step 1: Find closest ancestor with the same character
        def dfs_reparent(u: int):
            char = s[u]
            prev_ancestor = last_seen.get(char, -1)
            
            if prev_ancestor != -1:
                new_parent[u] = prev_ancestor
                
            last_seen[char] = u
            for v in adj[u]:
                dfs_reparent(v)
                
            # Backtrack to keep ancestor state valid for other branches
            if prev_ancestor == -1:
                del last_seen[char]
            else:
                last_seen[char] = prev_ancestor
                
        dfs_reparent(0)
        
        # Step 2: Build the updated tree and count subtree sizes
        new_adj = [[] for _ in range(n)]
        for i in range(1, n):
            new_adj[new_parent[i]].append(i)
            
        ans = [1] * n
        def dfs_size(u: int) -> int:
            for v in new_adj[u]:
                ans[u] += dfs_size(v)
            return ans[u]
            
        dfs_size(0)
        return ans