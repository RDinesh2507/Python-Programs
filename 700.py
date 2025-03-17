class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        cur_node = root
        while cur_node:
            if cur_node.val == val:
                return cur_node
            elif cur_node.val < val:
                cur_node = cur_node.right
            else:
                cur_node = cur_node.left