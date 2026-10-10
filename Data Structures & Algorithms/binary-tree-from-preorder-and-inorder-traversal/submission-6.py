# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_idx = {val: i for i, val in enumerate(inorder)}
        
        def helper(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end or in_start > in_end:
                return None
            
            node = TreeNode(preorder[pre_start])
            mid = inorder_idx[preorder[pre_start]]
            left_size = mid - in_start
            
            node.left = helper(pre_start + 1, pre_start + left_size, in_start, mid - 1)
            node.right = helper(pre_start + left_size + 1, pre_end, mid + 1, in_end)
            
            return node
            
        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)