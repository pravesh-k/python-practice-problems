## This problem is from LeetCode numbered #19. Remove Nth Node From End of List

# Problem Statement: Given the head of a linked list, remove the nth node 
# from the end of the list and return its head.

# Costraints:
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
                    
        count = listLen(head)
        newNode = head
        pos = 0
        
        if count == 1:
            return None
        
        if n == count:
            return head.next

        while pos < count - n -1:
            newNode = newNode.next
            pos += 1
            
        newNode.next = newNode.next.next
        
        return head


    def printList(self, head):

        while head != None:
            print(head.val, end=" ")
            head = head.next
        print()


def listLen(head):

    tempNode = head
    count = 0
    while tempNode:
        count += 1
        tempNode = tempNode.next

    return count


# driver code
def main():

    sol = Solution()

    head = ListNode(1)
    head.next = ListNode(2)
    # head.next.next = ListNode(3)
    # head.next.next.next = ListNode(4)
    # head.next.next.next.next = ListNode(5)
    # head.next.next.next.next.next = ListNode(6)

    n = 2

    sol.printList(sol.removeNthFromEnd(head, n))


if __name__ == "__main__":
    main()
