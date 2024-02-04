from LinkedList import singleLinkedList


def kthElem(ll, n):
    pointer1 = ll.head
    pointer2 = ll.tail
    for _ in range(n):
        if pointer2 is None:
            return None
        pointer2 = pointer2.next

    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1


llhere = singleLinkedList()
llhere.append(1)
llhere.append(2)
llhere.append(3)
llhere.append(4)
llhere.append(5)
llhere.append(6)
llhere.append(7)
llhere.append(8)
print(llhere)
print("Returning Kth value :- ")
print(kthElem(llhere, 3))
