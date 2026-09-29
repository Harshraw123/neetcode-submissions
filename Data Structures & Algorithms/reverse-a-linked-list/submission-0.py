# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:


        start=head

        if head==None:
            return None
        prev=None

        while start:

            fut=start.next

            start.next=prev

            prev=start

            start=fut

        return prev        



        