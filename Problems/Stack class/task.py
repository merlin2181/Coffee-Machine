class Stack():

    def __init__(self):
        self.list = []

    def push(self, el):
        self.list.append(el)

    def pop(self):
        return self.list.pop()

    def peek(self):
        return self.list[-1]

    def is_empty(self):
        if len(self.list) > 0:
            return False
        return True