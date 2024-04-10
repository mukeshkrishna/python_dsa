
def c(n,r):
    if r == 0 or n == r:
        return  1
    else:
        return c(n-1,r-1)+c(n-1,r)