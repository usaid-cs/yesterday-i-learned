class Node:
    val = None
    next = None


class MyLinkedList:

    head = None

    def __init__(self):
        """
        Initialize your data structure here.
        """


    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        # self.printList()
        if not self.head:
            return -1
        at_index = 0
        head = self.head
        while at_index <= index:
            if not head:
                return -1
            if at_index == index:
                return head.val
            head = head.next
            at_index += 1
        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = Node()
        node.val = val
        node.next = self.head
        self.head = node
        # self.printList()

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = Node()
        node.val = val
        if not self.head:
            self.head = node
            # self.printList()
            return
        head = self.head
        while True:
            if not head.next:
                break
            head = head.next
        head.next = node
        # self.printList()

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        node = Node()
        node.val = val
        if index == 0:
            if not self.head:
                self.head = node
                # self.printList()
                return
            if self.head:
                head = self.head
                self.head = node
                self.head.next = head
                return
        at_index = 0
        head = self.head
        while at_index <= index:
            # print("index is", at_index, index, head.val)
            if at_index == index - 1:
                next = head.next
                head.next = node
                node.next = next
                # self.printList()
                return
            head = head.next
            at_index += 1
        # self.printList()

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        at_index = 0
        head = self.head
        prev = None
        if index == 0:
            if not self.head:
                return
            if self.head:
                self.head = self.head.next
                return
        while at_index <= index:
            if not head:
                return
            if at_index == index:
                if not prev:
                    self.head = None
                    # self.printList('a')
                    return
                next = head.next
                prev.next = next
                # self.printList('b')
                return
            prev = head
            head = head.next
            at_index += 1
        # self.printList('c')

    def printList(self, tag=''):
        print(tag, end=' ')
        head = self.head
        while head:
            print(head.val, end='')
            head = head.next
        print()
