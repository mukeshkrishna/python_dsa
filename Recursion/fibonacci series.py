

# 0 1 1 2 3 5 8 13
# 0 1 2 3 4 5 6 7
def feb(n):
    i,j,count =0,1,2
    if n<=1:
        return n
    while count <= n:
        sum = i + j
        i = j
        j = sum
        count = count + 1
    print(j)


def feb_recr(n):
    if n <=1:
        return n
    else:
        return  feb_recr(n-2)+ feb_recr(n-1)

def fib_memoisation(n):
    global F
    if n <=1:
        F[n] = n
        return n
    else:
        if F[n-2] == -1:
            F[n-2] = fib_memoisation(n-2)
        if F[n-1] == -1:
            F[n-1] = fib_memoisation(n-1)
        return F[n-2] + F[n-1]




n = 10
F = [-1]*n
feb(10)

print(fib_memoisation(n))