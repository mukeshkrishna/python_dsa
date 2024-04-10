


def e(x,n):
    global s
    if n == 0:
        return s
    else:
        s = 1 + (x/n)*s
        return e(x,n-1)

s = 1
print(e(2,10))