
def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    # 随意选取一个基准数，比如选取列表第一个数
    base = nums[0]
    # left列表为nums中比基准数base小或等于base的数组成的列表
    left = [x for x in nums[1:] if x <= base]
    # right列表为nums中比基准数base大的数组成的列表
    right = [x for x in nums[1:] if x > base]
    # 对left和right列表递归排序
    return quick_sort(left) + [base] + quick_sort(right)

    #一行代码装逼
    # quick_sort = lambda array: array if len(array) <= 1 else quick_sort([
    #     item for item in array[1:] if item <= array[0]
    # ]) + [array[0]] + quick_sort([item for item in array[1:] if item > array[0]])


# print(quick_sort([2,5,9,3,7,1,5]))
#返回[1, 2, 3, 5, 5, 7, 9]

nums = [2,5,9,3,7,1,5]
left = [x for x in nums[:] if x >= 2 ]

print(left)