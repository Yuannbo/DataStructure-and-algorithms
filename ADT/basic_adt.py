class Node:
    def __init__(self,data):
        self.data =data
        self.next = None

class LinkedList:
    '''
    API
    -----------------------------------
    LinkedList(value)   创建一个链表
    is_empty()          链表是否为空
    length()            链表的长度
    insert(i,x)         在位置i插入x
    delete(i)           删除i
    update(i,x)         把下标为i的更新为x
    search(x)           在链表中查找x返回x的下标
    add_data(x)         头插法
    '''
    def __init__(self, val):
        self.__count = 1
        self.head = Node(val)

    def add_data(self,x):
        node = Node(x)
        node.next = self.head
        self.head = node
        self.__count += 1

    def delete(self,i):
        if i == 0:
            self.head = self.head.next
        elif i == self.length():
            pass
        else:
            pass



    def length(self):
        return self.__count

    def is_empty(self):
        return self.__count == 0

    def echo(self):
        while(self.head != None):
            print(self.head.data,end=' ')
            self.head = self.head.next



if __name__ == '__main__':
    linked = LinkedList(1)
    linked.add_data(2)
    linked.add_data(3)
    linked.add_data(4)
    linked.add_data(5)
    print(linked.length())
    linked.echo()


