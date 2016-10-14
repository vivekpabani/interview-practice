

class Node:

    def __init__(self, data, prev, next):

        self.data = data
        self.prev = prev
        self.next = next

 
class DoubleList():

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        node = Node(data, None, None)

        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node

    def __str__(self):
        node = self.head
        dlstr = ""
        while node:
            dlstr = dlstr + str(node.data)
            node = node.next
        return dlstr

    def reverse(self):
        temphead = self.tail
        temptail = self.head
        node = self.tail
        while node:
            temp = node.prev
            node.next, node.prev = node.prev, node.next
            node = temp 
        self.head = temphead
        self.tail = temptail


def main():

    dl = DoubleList()
    dl.append(1)
    dl.append(2)
    dl.append(3)
    dl.append(4)
    dl.append(5)
    print(dl)
    dl.reverse()
    print(dl)


main()
