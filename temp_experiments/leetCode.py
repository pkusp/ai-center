# encoding: utf-8
"""
@author: pkusp
@contact: pkusp@outlook.com

@version: 1.0
@file: leetCode.py
@time: 2018/8/14 下午10:07

这一行开始写关于本文件的说明与解释
"""


class ListNode(object):
    def __init__(self,val=None):
        self.val = val
        self.next = None


class TreeNode(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


def tree_to_list(root):
    if root is None:
        return []
    node_lst = []
    tmp = ListNode()
    head = tmp
    node_lst = in_order(root,tmp)
    return head


def in_order(root,node):
    if root.left:
        node = in_order(root.left,node)
        node.val = root.val
        node = node.next
    if root.right:
        node = in_order(root.right, node)
    return node


if __name__ == '__main__':
    root = TreeNode(1)
    l = TreeNode(2)
    r = TreeNode(3)
    root.left = l
    root.right = r
    node = tree_to_list(root)
    print(node)

