

def perm(nums):
    n = len(nums)
    res = []
    def helper(index):
        # base condition
        if index == n - 1:
            res.append(nums[:])
            return
        for j in range(index,n):
            nums[index], nums[j] = nums[j], nums[index]
            helper(index+1)
            nums[index], nums[j] = nums[j], nums[index]
    helper(0)
    return res

print(perm([1,2,3]))