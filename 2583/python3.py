# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        sums = []
        level_sum = 0
        level = 1
        nodes_visited = 0

        # Create an empty queue
        # for level order traversal
        queue = []

        # Enqueue Root and initialize height
        queue.append(root)

        while queue:


            # Print front of queue and
            # remove it from queue
            # print(queue[0].val, end=" ")
            if node is not None:
                level_sum += queue[0].val
            node = queue.pop(0)

            # # Enqueue left child
            if node.left is not None:
            queue.append(node.left)

            # # Enqueue right child
            if node.right is not None:
            queue.append(node.right)

            nodes_visited += 1
            if 2 ** level - 1== nodes_visited:
                level += 1
                sums.append(level_sum)
                level_sum = 0
        sums.append(level_sum) # last level
        
        if len(sums) < k:
            return -1
        else: 
            # print(sums)
            sums.sort(reverse=True)
            # print(sums)
            return sums[k-1]
            
