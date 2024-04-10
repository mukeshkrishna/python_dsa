
def print_n(n):
    if n > 0:
        print(n,end="")
        print_n(n - 1)

        print_n(n - 1)


print_n(3)
