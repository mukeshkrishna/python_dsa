# Time complexity is O(n) for squaring, and sorting is O(n log n), so over all Time complexity is O(n log n)
# Space complexity is O(n)
def sorted_squared_brute_force_sol_1(array):
    return sorted([ ele**2 for ele in array ])

print(sorted_squared_brute_force_sol_1([6,2,5,6]))


def sorted_squared_brute_force_sol_2(array):
    n = len(array)
    res = [0] * n # create an array and keep the elements as 0
    for i in range(n):
        res[i] = array[i] ** 2
    return res

print(sorted_squared_brute_force_sol_2([6,10,15,36]))


# With While Loop
def sorted_squared_optimal_solution_1(array):
    n = len(array)
    i,j = 0,n-1
    res = [0]*n
    while i <= j:
        ith_squared_ele = array[i] ** 2
        jth_squared_ele = array[j] ** 2
        if ith_squared_ele > jth_squared_ele:
            res[j-i] = ith_squared_ele
            i = i + 1
        else:
            res[j-i] = jth_squared_ele
            j = j - 1
    return res

# with for loop

def sorted_squared_optimal_solution_2(array):
    n = len(array)
    i, j = 0, n - 1
    res = [0]*n
    for k in reversed(range(n)): # range will be now 3,2,1,0 as we have reversed it
        if array[i]**2 > array[j]**2:
            res[k] = array[i]**2
            i = i + 1
        else:
            res[k] = array[j] ** 2
            j = j - 1
    return res

# Time complexity O(n) -> we are just traversing the array
# Space complexity O(n)


print(sorted_squared_optimal_solution_1([-9,-8,1,7]))