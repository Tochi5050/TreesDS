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
    def __init__(self):
        self.result_arr = []

    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []
        self.result_arr.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)
        return self.result_arr

result = Solution()
print(result.preorderTraversal(root))