# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        current = head

        while current:
            seen.add(current)
            if current.next in seen:
                return True
            current = current.next
        
        return False


        