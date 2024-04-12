def findTheWinner(n, k):
    # write code here
    array = [_ + 1 for _ in range(n)]

    def helper(array, start_index):
        if len(array) == 1:
            return array[0]
        index_to_remove = (start_index + k - 1) % len(array)

        del array[index_to_remove]
        return helper(array, index_to_remove)

    return helper(array, 0)
