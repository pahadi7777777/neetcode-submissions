"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        oldToNew = {}

        # Step 1: Create a copy of every node
        curr = head

        while curr:
            oldToNew[curr] = Node(curr.val)
            curr = curr.next

        # Step 2: Connect next and random pointers
        curr = head

        while curr:
            copy = oldToNew[curr]

            copy.next = oldToNew.get(curr.next)
            copy.random = oldToNew.get(curr.random)

            curr = curr.next

        return oldToNew.get(head)