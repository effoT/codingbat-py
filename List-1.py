
def first_last6(nums):
    if nums[0] == 6 or nums[-1] == 6:
        return True
    else:
        return False
# print(first_last([1, 2, 6]))
# print(first_last([6, 1, 2, 3]))
# print(first_last([13, 6, 1, 2, 3]))

def same_first_last(nums):
    if len(nums) < 1:
        return False
    elif nums[0] == nums[-1]:
        return True
    else:
        return False
# print(same_first_last([]))
# print(same_first_last([3,2,3]))

def make_pi():
    return [3,1,4]
# print(make_pi())

def common_end(a,b):
    if len(a) < 1 or len(b) < 1:
        return False
    elif (a[0] == b[0]) or (a[-1] == b[-1]):
        return True
    else:
        return False
# print(common_end([1, 2, 3], [7, 3]))
# print(common_end([1, 2, 3], [7, 3, 2]))

def sum3(nums):
    if len(nums) == 3:
        return nums[0] + nums[1] + nums[2]
    else:
        return False
# print(sum3([1, 2, 3]))
# print(sum3([5, 11, 2]))
# print(sum3([7, 0, 0]))
# print(sum3([7, 0]))

def rotate_left3(nums):
    new_nums = [1,2,3]
    new_nums[2] = nums[0]
    new_nums[0] = nums[1]
    new_nums[1] = nums[2]
    return new_nums
# print(rotate_left3([1, 2, 3]))
# print(rotate_left3([5, 11, 9]))
# print(rotate_left3([7, 0, 0]))
#
def reverse3(nums):
    return nums[::-1]
# print(reverse3([1, 2, 3]))
# print(reverse3([5, 11, 9]))
# print(reverse3([7, 0, 0]))
#
def max_end3(nums):
    if len(nums) != 3:
        return False
    elif nums[0] > nums[-1]:
        return [nums[0],nums[0],nums[0]]
    else:
        return [nums[-1],nums[-1],nums[-1]]
# print(max_end3([1, 2, 3]))
# print(max_end3([11, 5, 9]))
# print(max_end3([2, 11, 3]))

def sum2(nums):
    if len(nums) >= 2:
        return nums[0] + nums[1]
    elif len(nums) == 1:
        return nums[0]
    else:
        return 0
# print(sum2([1,2,3]))
# print(sum2([1,2]))
# print(sum2([1,1,1,1]))
# print(sum2([1]))
# print(sum2([]))

def middle_way(a,b):
    return [a[1],b[1]]
# print(middle_way([1, 2, 3], [4, 5, 6]))
# print(middle_way([7, 7, 7], [3, 8, 0]))
# print(middle_way([5, 2, 9], [1, 4, 5]))

def make_ends(nums):
    if sum(nums) >= 1:
        return [nums[0],nums[-1]]
    else:
        return False
# print(make_ends([1, 2, 3]))
# print(make_ends([1, 2, 3, 4]))
# print(make_ends([7, 4, 6, 2]))

def has23(nums):
    if 2 in nums or 3 in nums:
        return True
    else:
        return False
# print(has23([2,5]))
# print(has23([4,3]))
# print(has23([4,5]))
