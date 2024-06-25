class Stack():
    def __init__(self, capacity):
        self.capacity = capacity
        self.item = []

    def is_empty(self):
        return len(self.item) == 0

    def is_full(self):
        return len(self.item) == self.capacity

    def pop(self):
        if self.is_empty():
            return None
        return self.item.pop()

    def push(self, item):
        if self.is_full():
            return None
        return self.item.append(item)

    def top(self):
        if self.is_empty():
            return None
        return self.item[-1]


stack1 = Stack(capacity=5)
stack1.push(1)
stack1.push(2)

print(stack1.is_empty())

print(stack1.top())
