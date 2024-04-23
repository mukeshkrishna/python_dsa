

def perm(nums):
    n = len(nums)
    res = []
    def helper(index):
        if index == n-1:
            res.append(nums[:])
        hash = {}
        for j in range(index,n):
            if nums[j] not in hash:
                hash[nums[j]] = True
                nums[index], nums[j] = nums[j], nums[index]
                helper(index+1)
                nums[index], nums[j] = nums[j], nums[index]
    helper(0)
    return res


print(perm([1,1,3]))
