def insertNodeAtPosition(llist, data, position):
    # Write your code here
    ptr = llist
    eh = None
    for i in range(position - 1):
        ptr = ptr.next
        eh = ptr.next
    ptr.next = SinglyLinkedListNode(data)
    ptr.next.next = eh
    return llist
