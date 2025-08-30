class Queue:
    def __init__(self, capacity):
        self.queue = []
        self.capacity = capacity

    def enqueue(self, value):
        if len(self.queue) >= self.capacity:
            print("Queue Overflow! Cannot enqueue", value)
        else:
            self.queue.append(value)
            print(value, "enqueued to queue.")

    def dequeue(self):
        if not self.queue:
            print("Queue Underflow! Queue is empty.")
            return None
        else:
            return self.queue.pop(0)

    def front(self):
        if not self.queue:
            print("Queue is empty.")
            return None
        else:
            return self.queue[0]

    def display(self):
        if not self.queue:
            print("Queue is empty.")
        else:
            print("Queue elements:", self.queue)


# Usage
q = Queue(5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()              # [10, 20, 30]
print("Dequeued:", q.dequeue())
q.display()              # [20, 30]
print("Front element:", q.front())