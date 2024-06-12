class BungeoBBangTl:
    def __init__(self, price):
        self.price = price
        self.sok = None
    def fill_this(self, what):
        self.sok = what


b1 = BungeoBBangTl(1000)
b2 = BungeoBBangTl(2000)
b1.fii_this("팥")
b2.fill_this("슈크림")
print(b1.sok)
print(b1.howmuch)
print(b2.sok)
print(b2.howmuch)
