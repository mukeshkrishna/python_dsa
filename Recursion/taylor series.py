


def e(x,n):
    global p,f
    if n == 0:
        return 1
    else:
        res = e(x,n-1)
        p = p * x
        f = f * n


if __name__== "__main__":
    p = 1
    f = 1