class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.length = 0
        self.oldest = 0
        self.buffer = []

    def append(self, item):
        if self.length == self.capacity:
            if self.oldest == self.capacity:
                self.oldest = 0
            self.buffer[self.oldest] = item
            self.oldest += 1
        else:
            self.buffer.append(item)
            self.length += 1

    def get(self):
        return self.buffer
