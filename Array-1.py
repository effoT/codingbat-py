# Problems presented by codingbat.com



'''
#########################################################################################################
first_last_6
Given an array of ints, return true if 6 appears as either the first or last element in the array. 
The array will be length 1 or more.
'''
def first_last_6(nums):
    if nums[0] == 6 or nums[-1] == 6:
        return True
    return False


if(first_last_6([1, 2, 6])) != True: print("first_last_6([1, 2, 6]) failed")
assert first_last_6([1, 2, 6]) == True, "first_last_6([1, 2, 6]) failed"
assert first_last_6([6, 1, 2, 3]) == True, "first_last_6([6, 1, 2, 3]) failed"
assert first_last_6([13, 6, 1, 2, 3]) == False, "first_last_6([13, 6, 1, 2, 3]) failed"
assert first_last_6([13, 6, 1, 2, 6]) == True, "first_last_6([13, 6, 1, 2, 6]) failed"
assert first_last_6([3, 2, 1]) == False, "first_last_6([3, 2, 1]) failed"
assert first_last_6([3, 6, 1]) == False, "first_last_6([3, 6, 1]) failed"
assert first_last_6([3, 6]) == True, "first_last_6([3, 6]) failed"
assert first_last_6([3]) == False, "first_last_6([3]) failed"
assert first_last_6([5, 6]) == True, "first_last_6([5, 6]) failed"
assert first_last_6([5, 5]) == False, "first_last_6([5, 5]) failed"
assert first_last_6([1, 2, 3, 4, 6]) == True, "first_last_6([1, 2, 3, 4, 6]) failed"
assert first_last_6([1, 2, 3, 4]) == False, "first_last_6([1, 2, 3, 4]) failed"


''' 
#########################################################################################################
same_first_last 
Given an array of ints, return true if the array is length 1 or more, 
and the first element and the last element are equal.
'''

def same_first_last(nums):

    if nums == []:
        return False
    elif nums[0] == nums[-1]:
        return True
    return False


if(same_first_last([1, 2, 3])) != False: print("same_first_last([1, 2, 3]) failed")
if(same_first_last([1, 2, 3, 1])) != True: print("same_first_last([1, 2, 3, 1])  failed")
if(same_first_last([1, 2, 1])) != True: print("same_first_last([1, 2, 1]) failed")
if(same_first_last([7])) != True: print("same_first_last([7]) failed")
if(same_first_last([])) != False: print("same_first_last([]) failed")
if(same_first_last([1, 2, 3, 4, 5, 1])) != True: print("same_first_last([1, 2, 3, 4, 5, 1]) failed")
if(same_first_last([1, 2, 3, 4, 5, 13])) != False: print("same_first_last([1, 2, 3, 4, 5, 13]) failed")
if(same_first_last([13, 2, 3, 4, 5, 13])) != True: print("same_first_last([13, 2, 3, 4, 5, 13]) failed")
if(same_first_last([7, 7])) != True: print("same_first_last([7, 7]) failed")

'''
#########################################################################################################
make_pi 
Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.
'''

def make_pi():
    return [3,1,4]

if make_pi() != [3,1,4]: print("make_pi() failed")

'''
#########################################################################################################
common_end

Given 2 arrays of ints, a and b, return true if they have the same first element or they have the same last element. 
Both arrays will be length 1 or more.
'''
def common_end(a,b):
    if a[0] == b[0] or a[-1] == b[-1]:
        return True
    return False

if common_end([1, 2, 3], [7, 3]) != True: print("common_end([1, 2, 3], [7, 3]) failed")
if common_end([1, 2, 3], [7, 3, 2]) != False: print("common_end([1, 2, 3], [7, 3, 2]) failed")
if common_end([1, 2, 3], [1, 3]) != True: print("common_end([1, 2, 3], [1, 3]) failed")
if common_end([1, 2, 3], [1]) != True: print("common_end([1, 2, 3], [1]) failed")
if common_end([1, 2, 3], [2]) != False: print("common_end([1, 2, 3], [2]) failed")


'''
#########################################################################################################
sum3
Given an array of ints length 3, return the sum of all the elements.
'''

def sum3(nums):
    return nums[0] + nums[1] + nums[2]

if sum3([1, 2, 3]) != 6: print("sum3([1, 2, 3]) not 6")
if sum3([5, 11, 2]) != 18: print("sum3([5, 11, 2]) not 18")
if sum3([7, 0, 0]) != 7: print("sum3([7, 0, 0]) not 7")
if sum3([1, 2, 1]) != 4: print("sum3([1, 2, 1]) not 4")
if sum3([1, 1, 1]) != 3: print("sum3([1, 1, 1]) not 3")
if sum3([2, 7, 2]) != 11: print("sum3([2, 7, 2]) not 11")

'''
#########################################################################################################
this seems to be the pretty much same as list-1 on python side....
'''
