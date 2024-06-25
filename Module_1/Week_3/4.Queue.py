class Queue():
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def is_empty(self):
        return len(self.items) == 0          # true or false

    def is_full(self):
        return len(self.items) == self.capacity   # true or false

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def enqueue(self, item):
        if self.is_full():
            return None
        return self.items.append(item)

    def front(self):
        if self.is_empty():
            return None
        return self.items[0]


queue1 = Queue(capacity=5)
queue1.enqueue(1)

queue1.enqueue(2)

print(queue1.is_empty())
print(queue1.front())
print(queue1.dequeue())
