class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def __len__(self):
        node = self.head
        length = 0
        while node:
            node = node.next
            length += 1
        return length

    def add_at_head(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def add_at_end(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            p = self.head
            while p.next:
                p = p.next
            p.next = node


    def echo(self):
        node  = self.head
        while node:
            print(node.data,end=" ")
            node = node.next

    def length(self):
        return len(self)

    def is_empty(self):
        return len(self) == 0

if __name__ == '__main__':
    l1 = SinglyLinkedList()
    l1.add_at_end(1)
    l1.add_at_end(2)
    l1.add_at_end(3)
    l1.add_at_end(4)
    print(l1.length())
    print(l1.is_empty())
    l1.echo()
