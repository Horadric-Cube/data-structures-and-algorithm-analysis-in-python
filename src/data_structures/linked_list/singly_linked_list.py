class ListNode(object):
    def __init__(self, val: int = 0, next: "ListNode" = None) -> None:
        self.val = val
        self.next = next


class SinglyLinkedList(object):
    def __init__(self):
        # dummy head node.
        self.head_ = ListNode()
        self.tail_ = self.head_
        self.size_ = 0

    def size(lst: "SinglyLinkedList") -> int:
        """returns the number of elements in the list."""
        pass

    def clear(node: ListNode, lst: "SinglyLinkedList") -> None:
        """removes all elements from the list."""
        pass

    def empty() -> bool:
        """returns true if the list contains no elements, and false otherwise."""
        pass

    def push_back(node: ListNode) -> None:
        """adds node to the end of the list."""
        pass

    def pop_back() -> None:
        """removes the object at the end of the list."""
        pass

    def back() -> ListNode:
        """returns the object at the end of the list."""
        pass

    def front() -> ListNode:
        """returns the object at the front of the list."""
        pass

    def push_front(node: ListNode) -> None:
        """adds node to the front of the list."""
        pass

    def pop_front() -> None:
        """removes the object at the front of the list."""
        pass
