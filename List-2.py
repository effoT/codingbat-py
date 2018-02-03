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
print(centered_average([1, 2, 3, 4, 100]))
print(centered_average([1, 1, 5, 5, 10, 8, 7]))    
print(centered_average([-10, -4, -2, -4, -2, 0]))    
    