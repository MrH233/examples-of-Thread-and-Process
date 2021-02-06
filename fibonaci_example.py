"""five ways to give fibonaci list"""


# 1.iterator
class Fibo:
    def __init__(self):
        self.count = 0
        self.num_pre = 1
        self.num_aft = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == 1:
            internal = self.num_aft
            self.num_aft += self.num_pre
            self.num_pre = internal
            return self.num_aft
        else:
            self.count += 1
            return 1


x = Fibo()
for i in range(10000):
    print(next(x))


# 2.generator
def fibonaci(n):
    count = 1
    a, b = 1, 1
    while count <= n:
        yield b
        a, b = b, a + b
        count += 1


g = fibonaci(10000)  # Don't forget to initialize
for i in range(10000):
    print(next(g))


# 3.recursion (too slow)
def fibonaci2(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return fibonaci2(n - 1) + fibonaci2(n - 2)


# for i in range(1, 100):
#     print(fibonaci2(i))

# 4.locals()   the most easy way
locals()["x0"] = 1
for i in range(1, 10001):
    locals()[f"x{i}"] = locals()[f"x{i - 1}"] + locals()[f"x{i - 2}"] if i > 1 else 2
    print(f"方法三:{locals()[f'x{i - 1}']}")

# 5.loop        the most basic way
a, b = 0, 1
count, n = 1, 100
while count <= n:
    a, b = b, a + b
    print(b)
    count += 1

"""With large amount of data testing, basic loop is fastest.
And iterator have advantage with the increasing of data amount,
totally the second choice.And locals() and generator are the 
same method in the eyes of machine, they can be third choice.
While the recursion is the worst choice anyway,regardless of 
resources or speed."""
