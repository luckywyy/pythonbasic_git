

# 给定二叉搜索树的根结点 root，返回值位于范围 [low, high] 之间的所有结点的值的和。







# 给定根节点 进行二叉树的搜索

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(val=1)
root.left = TreeNode(val=3)
root.left.right = TreeNode(val=1)
low, high = 1, 2
res = 0
def LDR(root):
    global res
    if root == None:
        return
    elif root.val >= low and root.val <= high:
        res += root.val
    if root.left != None:
        LDR(root.left)

    if root.right != None:
        LDR(root.right)


LDR(root)
print(res)


# 不行的话 记得用self关键字

