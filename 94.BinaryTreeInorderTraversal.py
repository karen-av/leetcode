"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.


Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]


:type root: TreeNode
:rtype: List[int]
        
"""

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


def inorderTraversal(root):
    #tmp = []
    def func(r):
        return func(r.left) + [r.val] + func(r.right) if r else []
        #if r == None:
        #    return
        #func(r.left)
        #tmp.append(r.val)
        #func(r.right)
        #return tmp
    return func(root)
    #return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right) if root else []
       



    
   
    

x_v = TreeNode(1, TreeNode(2), TreeNode(3))

print(inorderTraversal(x_v))