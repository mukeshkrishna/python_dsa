

def kth_symbol(n,k):
    if n == 1:
        return 0
    l = 2 ** (n-1)
    mid = l // 2
    if k <= mid:
        return kth_symbol(n-1,k)
    else:
        return int(not kth_symbol(n-1,k-mid))
