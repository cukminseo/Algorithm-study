class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def insert1(where, data):
    global head
    newNode = Node(data)
    pre = head
    for _ in range(where - 1):
        pre = pre.next
    newNode.next = pre.next
    pre.next = newNode

def insert2(whatnext, data):
    global head
    newNode = Node(data)
    pre= head
    while pre.data!=whatnext:
        pre=pre.next
    newNode.next = pre.next
    pre.next = newNode


def delete(data):
    global head
    pre= head
    while pre.next.data!=data:
        pre= pre.next
    pre.next = pre.next.next

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

head = node1

insert1(3, "자료")
insert2("자료","구조")
delete("자료")
while head:
    print(head.data)
    head = head.next
