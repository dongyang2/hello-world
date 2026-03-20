# https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/description/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeNodeDIY(TreeNode):
    """不对不对，这个题目是不需要插入的，是直接从数组转为一个平衡二叉搜索树即可。"""
    def __init__(self, val=None, left=None, right=None):
        super().__init__(val, left, right)
        self.height = 0

    def insert(self, num):
        if self.val is None:
            self.val = num
            self.height += 1
        else:
            if num < self.val:
                left_height = self.left.insert(num)
                self.height = max(left_height, self.right.height) + 1
            else:
                right_height = self.right.insert(num)
                self.height =  max(self.left.height, right_height) + 1
        return self.height

    def check(self):
        if abs(self.left.height - self.right.height) > 1:
            self.turn()

    def turn(self):
        """因为我们知道了增序，那么只需要 调整左边 的就可以了"""



def gen_tree(nums):
    if len(nums) == 1:
        node = TreeNode(nums[0])
    elif len(nums) == 0:
        node = None
    else:
        mid = int(len(nums)/2)
        node = TreeNode(nums[mid])
        node.left = gen_tree(nums[:mid])
        node.right = gen_tree(nums[mid+1:])
    return node

def ergodic_tree_mid(node: TreeNode, li: list):
    """遍历树(中序)"""
    if node.left is not None:
        ergodic_tree_mid(node.left, li)
    li.append(node.val)
    if node.left is None and node.right is None:
        return
    if node.right is not None:
        ergodic_tree_mid(node.right, li)

def find_num(n:int, node:TreeNode):
    if node is not None:
        print(f"当前节点 {node.val}")
        if n < node.val:
            print("进入左子树")
            find_num(n, node.left)
        elif n == node.val:
            print("找到了")
        else:
            print("进入右子树")
            find_num(n, node.right)
    else:
        print("走到头了")


if __name__ == '__main__':
    li1 = [-10,-3,0, 1,5,9]
    # li1 = [1, 3]
    node1 = gen_tree(li1)
    li2 = []
    ergodic_tree_mid(node1, li2)
    print(f"中序遍历结果 {li2}")

    find_num(-3, node1)
