## This problem is from LeetCode numbered #876. Middle of the Linked List

# Problem Statement: Given the head of a singly linked list, return the middle node 
# of the linked list. If there are two middle nodes, return the second middle node.

# Costraints:
# The number of nodes in the list is in the range [1, 100].
# 1 <= Node.val <= 100

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow = fast = head

        # using the concept of fast and slow pointer, we can say slow pointer will 
        # reach middle node when fast node reaches last node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def printList(self, head):

        while head != None:
            print(head.val, end=" ")
            head = head.next
        print()


# driver code
def main():

    sol = Solution()

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    # head.next.next.next.next.next = ListNode(6)

    sol.printList(sol.middleNode(head))


if __name__ == "__main__":
    main()
