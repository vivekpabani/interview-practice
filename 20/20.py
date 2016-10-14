

class Node:

    def __init__(self, data, next):

        self.data = data
        self.next = next

 
class LinkedList():

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        node = Node(data, None)

        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node

        self.tail = node  

    def __str__(self):
        node = self.head
        lstr = ""
        while node is not None:
            lstr = lstr + str(node.data)
            node = node.next
        return lstr


def reverse_k(

def merge_ll(l1, l2):

    # if any list is empty, return the other.
    if not l1.head:
        return l2
    if not l2.head:
        return l1

    node1 = l1.head 
    node2 = l2.head 

    # We are modifying the l1 by inserting l2 nodes wherever necessary.

    # check if need to change the l1 head because l2 head is small. 
    if l1.head.data > node2.data:
        temp = node2
        node2 = node2.next
        l1.head = temp 
        l1.head.next = node1

    # go through l2: 
    # if current l2 node is less than l1 node, insert it.
    # otherwise go next in l1.
    # repeat till one list is empty 

    while node1.next and node2:
        if node2.data < node1.next.data:
            temp = node1.next
            node1.next = node2
            node2 = node2.next
            node1.next.next = temp
        node1 = node1.next

    # add the remaining nodes of l2 to l1 in case still some left.
    while node2:
        node1.next = node2
        node2 = node2.next 

    return l1     

def main():

    l1 = LinkedList()
    l1.append(1)
    l1.append(3)
    l1.append(5)
    l1.append(7)

    l2 = LinkedList()
    l2.append(2)
    l2.append(4)
    l2.append(6)
    l2.append(8)

    print("List1 : " +  str(l1))
    print("List2 : " +  str(l2))

    ll = merge_ll(l1, l2)

    print("Merged List : " + str(ll))

main()
