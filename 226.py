class Solution(object):
    def invertTree(self, root):
        if not root or (not root.left and not root.right):
            return root
        tmp = root.left
        root.left = root.right
        root.right = tmp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root