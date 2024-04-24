from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def to_list(head: Optional["ListNode"]):
        res = []
        current_node = head
        while current_node is not None:
            res.append(current_node.val)
            current_node = current_node.next
        return res


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        current_node = head
        last_valid_node = None
        res_head_node = None
        while current_node is not None:
            if current_node.val != val:
                if last_valid_node is not None:
                    last_valid_node.next = current_node
                else:
                    res_head_node = current_node
                last_valid_node = current_node
            current_node = current_node.next
        if last_valid_node is not None:
            last_valid_node.next = None
        return res_head_node
