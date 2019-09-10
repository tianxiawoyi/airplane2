def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    middle = int(len(lst)/2)

    left = merge_sort(lst[ :middle])#左边
    right = merge_sort(lst[middle: ])#右边
    merged = []
    while left and right:
        merged.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
    merged.extend(right if right else left)  #该方法没有返回值，但会在已存在的列表中添加新的列表内容
    return merged


def quick_sort(nums):
    '''
    快速排序:分而治之
    在数组中寻找一个 基准数,
    将小于基准数 放左边 组成一个数组,然后这个数组继续这样
    将大于基准数 放右边 组成一个数组,然后这个数组继续这样
    分成不能分了再组合在一起
    '''
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


if __name__ == '__main__':
    # data_lst = [6,202,100,301,38,8,1]
    # print(merge_sort(data_lst))

    left = [6,5,3]
    right = [2,4,7]
    merged=[]
    merged.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
    print(merged)

    ss = left.pop(0) if left[0] <= right[0] else right.pop(0)
    print(ss)