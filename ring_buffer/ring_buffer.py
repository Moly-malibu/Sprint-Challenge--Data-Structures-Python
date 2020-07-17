class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None] * capacity
        
    def append(self, item):
        if self.current == self.capacity:
            self.current = 0
        self.storage[self.current] = item
        self.current += 1
        
    def get(self):
        for i in self.storage:
            if i is None:
                self.storage.remove(1)
        return self.storage
        pass

buffer = RingBuffer(5);
#buffer.get()
buffer.append('a')
buffer.append('b')
buffer.append('c')
#buffer.get()
buffer.append('d')
#buffer.get()
buffer.append('e')
buffer.append('f')
buffer.get()
print(buffer.get())