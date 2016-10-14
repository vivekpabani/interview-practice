

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

def add_one_rec(node):

    if not node.next:
        carry = int((node.data + 1)/10)
        node.data = (node.data + 1)%10 
        return carry 
    else:
        temp_carry = add_one_rec(node.next) 

        carry = int((node.data + temp_carry)/10)
        node.data = (node.data + temp_carry)%10
        return carry

def add_one(ll):

    add_one_rec(ll.head) 

def main():

    ll = LinkedList()
    ll.append(1)
    ll.append(9)
    ll.append(9)
    ll.append(9)
    print(ll)
    add_one(ll)
    print(ll)
main()
