__author__ = 'trunghieu11'

class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def maxSum(node):
    if node == None:
        return 0
    return node.value + max(maxSum(node.left), maxSum(node.right))

if __name__ == '__main__':
    root = Node(0)
    print maxSum(root)