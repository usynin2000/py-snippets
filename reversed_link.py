from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next - next


class Solution:
    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev


def create_linked_list(arr: list):
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head
    for num in arr[1:]:
        current.next = ListNode(num)
        current = current.next
    return head


def linked_list_to_list(head: Optional[ListNode]) -> list:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


if __name__ == "__main__":
    input_list = [0, 1, 2, 3, 4]

    head = create_linked_list(input_list)

    sol = Solution()
    reversed_head = sol.reverse_list(head)

    print("Reversed list:", linked_list_to_list(reversed_head))