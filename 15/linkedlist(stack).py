class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def peep(self):
        return self.top.data

    def pop(self):
        data = self.top.data
        self.top = self.top.next
        return data
a = Stack()

a.push(10)
a.push(20)
a.push(30)

print(a.peep())
a.pop()
print(a.peep())
