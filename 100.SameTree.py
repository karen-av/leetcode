"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Input: p = [1,2,3], q = [1,2,3]
Output: true

Input: p = [1,2], q = [1,null,2]
Output: false

Input: p = [1,2,1], q = [1,1,2]
Output: false
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False

    def func(root):
        return [root.val] + func(root.left) +  func(root.right) if root else [None]
    
    a, b = func(p), func(q)
    for i, n in enumerate(a):
        if a[i] != b[i]:
            return False
    return True

        


a = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
b = TreeNode(1, None, TreeNode(2))

c = TreeNode(1, TreeNode(2), TreeNode(3))
d = TreeNode(1, TreeNode(2), TreeNode(3))

print(isSameTree(c,d))

