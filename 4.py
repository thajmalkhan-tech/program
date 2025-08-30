class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear:
            self.rear.next = new_node
        self.rear = new_node
        if not self.front:
            self.front = new_node

    def dequeue(self):
        if not self.front:
            return "Queue is Empty"
        data = self.front.data
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return data

    def display(self):
        current = self.front
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

# Example
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.dequeue()
q.display()