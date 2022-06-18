# queue using Linked List
class Node:
    def __init__(self, value):
        self.key = value
        self.next = None


class Queue:
    def __init__(self):
        self.start = None

    def Enqueue(self, value):

        new_node = Node(value)

        if self.start is None:
            self.start = new_node
            new_node.next = self.start
            print("New Node added")
            return

        temp = self.start
        while temp.next is not self.start:
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
        print("New Node added")
        return

    def display(self):
        if self.start:
            temp = self.start
            while temp.next != self.start:
                print(temp.key)
                temp = temp.next
            print(temp.key)
        else:
            print("Queue is Empty")

    def Dequeue(self):
        if self.start:
            if self.start.next == self.start:
                self.start = None
            else:
                temp = self.start
                while temp.next is not self.start:
                    temp = temp.next
                temp.next = temp.next.next
                self.start = self.start.next
        else:
            return


if __name__ == "__main__":
    q = Queue()
    q.Enqueue(4)
    q.Enqueue(5)
    q.Enqueue(7)
    q.Enqueue(1)
    q.Enqueue(6)
    print("Before dequeue")
    q.display()
    q.Dequeue()
    print("After dequeue")
    q.display()
