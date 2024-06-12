class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def addNode(data):
    global head, where
    newNode = Node(data)
    if head is None:
        head = newNode
    else:
        where = head
        while where.next:
            where = where.next
        where.next = newNode
    return newNode

head = None

for now in range(1,42):
    last = addNode(now)
last.next = head