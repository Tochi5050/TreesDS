# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
n8 = TreeNode(8)
n9 = TreeNode(9)
n10 = TreeNode(10)

# Connect left and right children
n1.left = n2
n1.right = n3

n2.left = n4
n2.right = n5

n3.left = n6
n3.right = n7

n4.left = n8
n4.right = n9

n5.left = n10

root = n1

class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []
        stack = []
        res = []
        stack.append(root)

        while stack:
            nodev = stack[-1]
            if nodev.right is None and nodev.left is None:
                nodepop = stack.pop()
                res.append(nodepop.val)
                continue

            if (nodev.right is not None and nodev.right.val in res) or (nodev.left is not None and nodev.left.val in res):
                nodepop = stack.pop()
                res.append(nodepop.val)
                continue

            if nodev.right is not None and nodev.right.val not in res:
                stack.append(nodev.right)

            if nodev.left is not None and nodev.left.val not in res:
                stack.append(nodev.left)

        print(res)





result = Solution()
print(result.postorderTraversal(root))
