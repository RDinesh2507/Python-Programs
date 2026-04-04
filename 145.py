# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import typing
class Solution:
    def postorderTraversal(self, root: typing.Optional[TreeNode]) -> typing.List[int]: # type: ignore
        def dfs(root):
            if root is None:
                return
            dfs(root.left)
            dfs(root.right)
            ans.append(root.val)
        ans=[]
        dfs(root)
        return ans