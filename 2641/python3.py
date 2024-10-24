# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_child_sum(self, node):
        if node.right is not None:
            r = node.right.val
        else:
            r = 0
        if node.left is not None:
            l = node.left.val
        else:
            l = 0
        return r + l
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # bfs
        bfs_queue = [root]
        sums = []

        while bfs_queue:
            n = len(bfs_queue)
            level_sum = 0
            # traverse the level
            for _ in range(n):
                node = bfs_queue.pop(0)
                level_sum += node.val

                if node.left is not None:
                    bfs_queue.append(node.left)
                if node.right is not None:
                    bfs_queue.append(node.right)
            sums.append(level_sum)
        
        # bfs 2
        bfs2_queue = [root]
        level = 0
        sibling_sums = [root.val]

        while bfs2_queue:
            n = len(bfs2_queue)
            
            for _ in range(n):
                node = bfs2_queue.pop(0)
                s = sibling_sums.pop(0)
                # replace
                node.val = sums[level] - s
                # get child sum
                child_sum = self.get_child_sum(node)
                # queue
                if node.left is not None:
                    bfs2_queue.append(node.left)
                    sibling_sums.append(child_sum)
                if node.right is not None:
                    bfs2_queue.append(node.right)
                    sibling_sums.append(child_sum)
            level += 1
                
        # # dfs
        # dfs_stack = [root]
        # visited = set()
        # level = 0
        # sibling_stack = [root.val]

        # while dfs_stack:
        #     node = dfs_stack.pop()
        #     sibling_sum = sibling_stack.pop()
        #     # check if visited
        #     if node in visited:
        #         level -= 1 # move up a level
        #         continue
        #     # if not visited
        #     # replace
        #     print(node.val, level, sums)
        #     node.val = sums[level] - sibling_sum
        #     visited.add(node)
        #     # stack children
        #     if node.right is not None and node.left is not None:
        #         s = node.right.val + node.left.val
        #     if node.right is not None:
        #         dfs_stack.append(node.right)
        #         sibling_stack.append(s)
        #     if node.left is not None:
        #         dfs_stack.append(node.left)
        #         sibling_stack.append(s)
        #     level += 1 # move down a level

        return root
        
        
