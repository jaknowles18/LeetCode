class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def recursive_call(root, count):
            if root is None:
                return count

            left = recursive_call(root.left, count + 1)
            if left == -1:
                return -1

            right = recursive_call(root.right, count + 1)
            if right == -1:
                return -1

            if abs(left - right) > 1:
                return -1

            return max(left, right)

        return recursive_call(root, 0) != -1