class Node:
    def __init__(self, value, next=None):
        self.next = next
        self.value = value


def createLinkedList(A):
    prev = None
    cur = None
    for i in range(len(A) - 1, -1, -1):
        cur = Node(A[i], prev)
        prev = cur
    return cur