class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            return "Stack is Empty"
        data = self.top.data
        self.top = self.top.next
        return data

    def display(self):
        current = self.top
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

# Example
s = Stack()
s.push(10)
s.push(20)
s.pop()
s.display()