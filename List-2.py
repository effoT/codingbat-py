def count_evens(nums):
    counter = 0
    for i in nums:
        if i % 2 == 0:
            counter += 1
    return counter
# print(count_evens([2, 1, 2, 3, 4]))
# print(count_evens([2, 2, 0]))
# print(count_evens([1, 3, 5]))

def big_diff(nums):
    return max(nums) - min(nums)
# print(big_diff([10, 3, 5, 6]))
# print(big_diff([7, 2, 10, 9]))
# print(big_diff([2, 10, 7, 2]))

def centered_average(nums):
    # get the total without min and max value
    centered_total = sum(nums) - (max(nums) + min(nums))
    # get the amount to divide the total with 
    divider = (len(nums) -2 )
    return centered_total // divider
# print(centered_average([1, 2, 3, 4, 100]))
# print(centered_average([1, 1, 5, 5, 10, 8, 7]))    
# print(centered_average([-10, -4, -2, -4, -2, 0]))    
    
def sum13(nums):
    result = 0
    for i in range(len(nums)):
        if nums[i] == 13: 
            continue
        # remember to check that the i is not 0 so that we will not check the last element in the list
        elif nums[(i - 1)] == 13 and i != 0:
            continue
        else:
            result += nums[i]
    return result
# print(sum13([1, 2, 2, 1]))
# print(sum13([1, 1]))
# print(sum13([1, 2, 2, 1, 13]))
# print(sum13([1, 2, 13, 2, 1, 13]))

def sum67(nums):
    result = 0
    lock = 0
    for i in range(len(nums)):
        if nums[i] == 6:
            lock = 1
        elif nums[i] == 7 and lock == 1:
            lock = 0
        elif lock == 1:
            continue
        elif lock == 0:
            result += nums[i]
    return result
# print(sum67([1, 2, 2]))
# print(sum67([1, 2, 2, 6, 99, 99, 7]))
# print(sum67([1, 1, 6, 7, 2]))
# print(sum67([2, 7, 6, 2, 6, 7, 2, 7]))

def has22(nums):
    for i in range(len(nums) -1):
        if nums[i] == 2 and nums[(i + 1)] == 2:
            return True
    return False
# print(has22([1, 2, 2]))
# print(has22([1, 2, 1, 2]))
# print(has22([2, 1, 2]))
