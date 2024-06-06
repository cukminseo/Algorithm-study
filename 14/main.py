import sys

sys.stdin = open("main.txt", 'r')


def preorder(T):
    if T:
        print("%d" % T, end=' ')
        preorder(Tree[T][0])
        preorder(Tree[T][1])


def inorder(T):
    if T:
        inorder(Tree[T][0])
        print("%d" % T, end=' ')
        inorder(Tree[T][1])


def postorder(T):
    if T:
        postorder(Tree[T][0])
        postorder(Tree[T][1])
        print("%d" % T, end=' ')


V, E = map(int, input().split())
Data = list(map(int, input().split()))
Tree = [[0] * 5 for _ in range(V + 1)]
for i in range(V + 1):
    Tree[i][3] = Tree[i][4] = -1
Tree[1][4] = 0
for i in range(E):
    parent, child = Data[i * 2:i * 2 + 2]

    if Tree[parent][0] == 0:
        Tree[parent][0] = child
        Tree[parent][2] += 1
        Tree[child][3] = parent
        Tree[child][4] = Tree[parent][4] + 1
else:
    Tree[parent][1] = child
    Tree[parent][2] += 1
    Tree[child][3] = parent
    Tree[child][4] = Tree[parent][4] + 1
preorder(1)
print()
inorder(1)
print()
postorder(1)
print()
for i in range(len(Tree)):
    print(Tree[i])
