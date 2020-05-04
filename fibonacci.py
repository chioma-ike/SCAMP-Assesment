# fibonacci sequence
# f = first number
# s = second number


def fibonacci():
    f = 0
    s = 1
    while True:
        yield f
        f = s
        s = f + s


for i in fibonacci():
    if i > 100000:
        break
    print(i, end=" ")
