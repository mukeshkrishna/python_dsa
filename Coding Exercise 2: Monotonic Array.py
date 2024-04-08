def monotonic_array(array):
    n = len(array)
    if n == 0 or n == 1:
        return True
    first = array[0]
    last = array[n-1]

    if first < last:
        # Monotonic Increasing, else Not monotonic
        for k in range(n-1):
            if array[k] > array [k+1]: return False
    elif first == last:
        # Monotonic if all values are same
        for k in range(n-1):
            if array[k] != array[k+1]: return False
    else:
        # Monotonic Decreasing, else not monotonic
        for k in range(n - 1):
            if array[k] < array[k+1]: return False
    return True
