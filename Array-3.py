# Problems presented by codingbat.com

'''
maxSpan 

Consider the leftmost and righmost appearances of some value in an array. 
We'll say that the "span" is the number of elements between the two inclusive.
A single value has a span of 1. Returns the largest span found in the given array. 
(Efficiency is not a priority.)
'''
def maxSpan(nums):
    if not nums:
        return 0
    
    longest_span = 0
    for o in range(0, len(nums)):
        # loop through the numbers
        for i in range(o, len(nums)):
            # compare the numbers with the rest of the array to find the longest span
            if nums[o] == nums[i]:
                # print("outer {}, inner {}".format(o, i))
                if i - o > longest_span:
                    longest_span = i - o
                    # print("new marked span {}".format(i-o))
    return longest_span + 1  # add one due to the reduction on the indexing

# if maxSpan([1, 2, 1, 1, 3]) != 4: print("maxSpan([1, 2, 1, 1, 3]) not 4")
# if maxSpan([1, 4, 2, 1, 4, 1, 4]) != 6: print("maxSpan([1, 4, 2, 1, 4, 1, 4]) not 6")
# if maxSpan([1, 4, 2, 1, 4, 4, 4]) != 6: print("maxSpan([1, 4, 2, 1, 4, 4, 4]) not 6")
# if maxSpan([3, 3, 3]) != 3: print("maxSpan([3, 3, 3]) not 3")
# if maxSpan([3, 9, 3]) != 3: print("maxSpan([3, 9, 3]) not 3")
# if maxSpan([3, 9, 9]) != 2: print("maxSpan([3, 9, 9]) not 2")
# if maxSpan([3, 9]) != 1: print("maxSpan([3, 9]) not 1")
# if maxSpan([3, 3]) != 2: print("maxSpan([3, 3]) not 2")
# if maxSpan([]) != 0: print("maxSpan([]) not 0")
# if maxSpan([1]) != 1: print("maxSpan([1]) not 1")

'''
fix34
Return an array that contains exactly the same numbers as the given array, but rearranged so that every 3 
is immediately followed by a 4. Do not move the 3's, but every other number may move. The array contains 
the same number of 3's and 4's, every 3 has a number after it that is not a 3, and a 3 appears in the array before any 4.
'''
def fix34(nums):
    for o in range(len(nums)):
        if nums[o] == 3 and nums[o+1] != 4:
            for i in range(len(nums)):
                if nums[i] == 4 and nums[i-1] != 3:
                    nums[i], nums[o+1] = nums[o+1], nums[i]
    return nums


# if fix34([1, 3, 1, 4]) != [1, 3, 4, 1]: print("fix34([1, 3, 1, 4]) not [1, 3, 4, 1]")
# if fix34([1, 3, 1, 4, 4, 3, 1]) != [1, 3, 4, 1, 1, 3, 4]: print("fix34([1, 3, 1, 4, 4, 3, 1]) not [1, 3, 4, 1, 1, 3, 4]")
# if fix34([3, 2, 2, 4]) != [3, 4, 2, 2]: print("fix34([3, 2, 2, 4] not [3, 4, 2, 2]")
# if fix34([3, 2, 3, 2, 4, 4]) != [3, 4, 3, 4, 2, 2]: print("fix34([3, 2, 3, 2, 4, 4]) not [3, 4, 3, 4, 2, 2]")
# if fix34([2, 3, 2, 3, 2, 4, 4]) != [2, 3, 4, 3, 4, 2, 2]: print("fix34([2, 3, 2, 3, 2, 4, 4]) not [2, 3, 4, 3, 4, 2, 2]")
# if fix34([5, 3, 5, 4, 5, 4, 5, 4, 3, 5, 3, 5]) != [5, 3, 4, 5, 5, 5, 5, 5, 3, 4, 3, 4]: print("fix34([5, 3, 5, 4, 5, 4, 5, 4, 3, 5, 3, 5]) not [5, 3, 4, 5, 5, 5, 5, 5, 3, 4, 3, 4]")
# if fix34([3, 1, 4]) != [3, 4, 1]: print("fix34([3, 1, 4]) not [3, 4, 1]")
# if fix34([3, 4, 1]) != [3, 4, 1]: print("fix34([3, 4, 1]) not [3, 4, 1]")
# if fix34([1]) != [1]: print("fix34([1]) not [1]")
# if fix34([]) != []: print("fix34([]) not []")
# if fix34([7, 3, 7, 7, 4]) != [7, 3, 4, 7, 7]: print("fix34([7, 3, 7, 7, 4]) not [7, 3, 4, 7, 7]")
# if fix34([3, 1, 4, 3, 1, 4]) != [3, 4, 1, 3, 4, 1]: print("fix34([3, 1, 4, 3, 1, 4]) not [3, 4, 1, 3, 4, 1]")
# if fix34([3, 1, 1, 3, 4, 4]) != [3, 4, 1, 3, 4, 1]: print("fix34([3, 1, 1, 3, 4, 4]) not [3, 4, 1, 3, 4, 1]")

'''
fix45
(This is a slightly harder version of the fix34 problem.) Return an array that contains exactly the same numbers as the given array,
but rearranged so that every 4 is immediately followed by a 5. Do not move the 4's, but every other number may move. 
The array contains the same number of 4's and 5's, and every 4 has a number after it that is not a 4. In this version, 
5's may appear anywhere in the original array.
'''
# the original code will fit here due to it's not interested if the number to be searched is before or after
def fix45(nums):
    for o in range(len(nums)):
        if nums[o] == 4 and nums[o+1] != 5:
            for i in range(len(nums)):
                if nums[i] == 5 and nums[i-1] != 4:
                    nums[i], nums[o+1] = nums[o+1], nums[i]
    return nums

# if fix45([5, 4, 9, 4, 9, 5]) != [9, 4, 5, 4, 5, 9]:print("fix45([5, 4, 9, 4, 9, 5]) not [9, 4, 5, 4, 5, 9]")
# if fix45([1, 4, 1, 5]) != [1, 4, 5, 1]: print("fix45([1, 4, 1, 5]) not [1, 4, 5, 1]")
# if fix45([1, 4, 1, 5, 5, 4, 1]) != [1, 4, 5, 1, 1, 4, 5]: print("fix45([1, 4, 1, 5, 5, 4, 1]) not [1, 4, 5, 1, 1, 4, 5]")
# if fix45([4, 9, 4, 9, 5, 5, 4, 9, 5]) != [4, 5, 4, 5, 9, 9, 4, 5, 9]: print("fix45([4, 9, 4, 9, 5, 5, 4, 9, 5]) not [4, 5, 4, 5, 9, 9, 4, 5, 9]")
# if fix45([5, 5, 4, 1, 4, 1]) != [1, 1, 4, 5, 4, 5]: print("fix45([5, 5, 4, 1, 4, 1]) not [1, 1, 4, 5, 4, 5]")
# if fix45([4, 2, 2, 5]) != [4, 5, 2, 2]: print("fix45([4, 2, 2, 5]) not [4, 5, 2, 2]")
# if fix45([4, 2, 4, 2, 5, 5]) != [4, 5, 4, 5, 2, 2]: print("fix45([4, 2, 4, 2, 5, 5]) not [4, 5, 4, 5, 2, 2]")
# if fix45([4, 2, 4, 5, 5]) != [4, 5, 4, 5, 2]: print( "fix45([4, 2, 4, 5, 5]) not [4, 5, 4, 5, 2]")
# if fix45([1, 1, 1]) != [1, 1, 1]: print("fix45([1, 1, 1]) not [1, 1, 1]")
# if fix45([4, 5]) != [4, 5]: print("fix45([4, 5]) not [4, 5]")
# if fix45([5, 4, 1]) != [1, 4, 5]: print("fix45([5, 4, 1]) not [1, 4, 5]")
# if fix45([]) != [] : print("fix45([]) not []")
# if fix45([5, 4, 5, 4, 1]) != [1, 4, 5, 4, 5]: print("fix45([5, 4, 5, 4, 1]) not [1, 4, 5, 4, 5]")
# if fix45([4, 5, 4, 1, 5]) != [4, 5, 4, 5, 1]: print("fix45([4, 5, 4, 1, 5]) not [4, 5, 4, 5, 1]")
# if fix45([3, 4, 5]) != [3, 4, 5]: print("fix45([3, 4, 5]) not [3, 4, 5]")
# if fix45([4, 1, 5]) != [4, 5, 1]: print("fix45([4, 1, 5]) not [4, 5, 1]")
# if fix45([5, 4, 1]) != [1, 4, 5]: print("fix45([5, 4, 1]) not [1, 4, 5]")
# if fix45([2, 4, 2, 5]) != [2, 4, 5, 2]: print("fix45([2, 4, 2, 5]) not [2, 4, 5, 2]")

'''
canBalance
Given a non-empty array, return true if there is a place to split the array so that the sum of the numbers 
on one side is equal to the sum of the numbers on the other side.
'''
def canBalance(nums):
    if not nums:
        return False
    for o in range(len(nums)):
        if sum(nums[o:]) == sum(nums[:o]):
            return True
    return False
            

# if canBalance([1, 1, 1, 2, 1]) != True: print("canBalance([1, 1, 1, 2, 1]) not True")
# if canBalance([2, 1, 1, 2, 1]) != False: print("canBalance([2, 1, 1, 2, 1]) not False")
# if canBalance([10, 10]) != True: print("canBalance([10, 10]) not True")
# if canBalance([10, 0, 1, -1, 10]) != True: print("canBalance([10, 0, 1, -1, 10]) not True")
# if canBalance([1, 1, 1, 1, 4]) != True: print("canBalance([1, 1, 1, 1, 4]) not True")
# if canBalance([2, 1, 1, 1, 4]) != False: print("canBalance([2, 1, 1, 1, 4]) not False")
# if canBalance([2, 3, 4, 1, 2]) != False: print("canBalance([2, 3, 4, 1, 2]) not False")
# if canBalance([1, 2, 3, 1, 0, 2, 3]) != True: print("canBalance([1, 2, 3, 1, 0, 2, 3]) not True")
# if canBalance([1, 2, 3, 1, 0, 1, 3]) != False: print("canBalance([1, 2, 3, 1, 0, 1, 3]) not False")
# if canBalance([1]) != False: print("canBalance([1]) no False")
# if canBalance([1, 1, 1, 2, 1]) != True: print("canBalance([1, 1, 1, 2, 1])  not True")

'''
linearIn
Given two arrays of ints sorted in increasing order, outer and inner, return true if all of the numbers in inner appear in outer.
 The best solution makes only a single "linear" pass of both arrays, 
 taking advantage of the fact that both arrays are already in sorted order.
'''
def linearIn(outer,inner):
    for o in range(len(inner)):
        if inner[o] not in outer:
            return False
    return True
    

# print(linearIn([1, 2, 4, 6], [2, 4]))
# print(linearIn([-1, 0, 3, 3, 3, 10, 12], [0, 3, 12, 14]))
# if linearIn([1, 2, 4, 6], [2, 4]) != True: print("linearIn([1, 2, 4, 6], [2, 4])  not True")
# if linearIn([1, 2, 4, 6], [2, 3, 4]) != False: print("linearIn([1, 2, 4, 6], [2, 3, 4])  not False")
# if linearIn([1, 2, 4, 4, 6], [2, 4]) != True: print("linearIn([1, 2, 4, 4, 6], [2, 4]) not True")
# if linearIn([2, 2, 4, 4, 6, 6], [2, 4]) != True: print("linearIn([2, 2, 4, 4, 6, 6], [2, 4]) not True")
# if linearIn([2, 2, 2, 2, 2], [2, 2]) != True:print("linearIn([2, 2, 2, 2, 2], [2, 2]) not Frue")
# if linearIn([2, 2, 2, 2, 2], [2, 4]) != False: print("linearIn([2, 2, 2, 2, 2], [2, 4]) not False")
# if linearIn([2, 2, 2, 2, 4], [2, 4]) != True: print("linearIn([2, 2, 2, 2, 4], [2, 4])  not True")
# if linearIn([1, 2, 3], [2]) != True: print("linearIn([1, 2, 3], [2])  not True")
# if linearIn([1, 2, 3], [-1]) != False: print("linearIn([1, 2, 3], [-1]) not False")
# if linearIn([1, 2, 3], []) != True: print("linearIn([1, 2, 3], []) not True")
# if linearIn([-1, 0, 3, 3, 3, 10, 12], [-1, 0, 3, 12]) != True: print("linearIn([-1, 0, 3, 3, 3, 10, 12], [-1, 0, 3, 12]) not True")
# if linearIn([-1, 0, 3, 3, 3, 10, 12], [0, 3, 12, 14]) != False: print("linearIn([-1, 0, 3, 3, 3, 10, 12], [0, 3, 12, 14]) not False")
# if linearIn([-1, 0, 3, 3, 3, 10, 12], [-1, 10, 11]) != False: print("linearIn([-1, 0, 3, 3, 3, 10, 12], [-1, 10, 11]) not False")

'''
squareUp
Given n>=0, create an array length n*n with the following pattern,
 shown here for n=3 : {0, 0, 1,    0, 2, 1,    3, 2, 1} (spaces added to show the 3 groups).
'''
def squareUp(num):
    if not num or num == 0:
        return []
    
    # array collection
    arrayCol = []

    # run from 1 to the required amount and fix the indexing when writing
    for o in range(1, num +1):

        # prep a temp array filled with the necessary amount of 0
        array = []
        for temp in range(num):
            array.append(0)
        
        for i in range(1, num +1): # set up the array with the current max number for the section
            if i <= o: # if the running value is in range with the "section" set the value otherwise leave it with it's prepped 0
                array[(i - 1)] = i
        arrayCol += array[::-1] # merge the array in reverse to the collection
    return arrayCol

# if squareUp(3) != [0, 0, 1, 0, 2, 1, 3, 2, 1]: print("squareUp(3) not [0, 0, 1, 0, 2, 1, 3, 2, 1]")
# if squareUp(2) != [0, 1, 2, 1]: print("squareUp(2) not [0, 1, 2, 1]")
# if squareUp(4) != [0, 0, 0, 1, 0, 0, 2, 1, 0, 3, 2, 1, 4, 3, 2, 1]: print("squareUp(4) not [0, 0, 0, 1, 0, 0, 2, 1, 0, 3, 2, 1, 4, 3, 2, 1]")
# if squareUp(1) != [1]: print("squareUp(1) not [1]")
# if squareUp(0) != []: print("squareUp(0) not []")
# if squareUp(6) != [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 1, 0, 0, 0, 3, 2, 1, 0, 0, 4, 3, 2, 1, 0, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1]: print("squareUp(6) not [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 1, 0, 0, 0, 3, 2, 1, 0, 0, 4, 3, 2, 1, 0, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1]")

'''
seriesUp 

Given n>=0, create an array with the pattern {1,    1, 2,    1, 2, 3,   ... 1, 2, 3 .. n} 
(spaces added to show the grouping). Note that the length of the array will be 1 + 2 + 3 ... + n,
 which is known to sum to exactly n*(n + 1)/2.
'''
def seriesUp(num):
    if not num or num == 0:
        return []

    arrayCol = []
    for o in range(num):
        array = []
        for i in range(o + 1):
            array.append(i + 1)
        arrayCol += array
    return arrayCol


# if seriesUp(4) != [1, 1, 2, 1, 2, 3, 1, 2, 3, 4]: print("seriesUp(4) not [1, 1, 2, 1, 2, 3, 1, 2, 3, 4]")
# if seriesUp(2) != [1, 1, 2]	: print("seriesUp(2) not [1, 1, 2]")
# if seriesUp(1) != [1]: print("seriesUp(1) not [1]")
# if seriesUp(0) != []: print("seriesUp(0) not []")
# if seriesUp(6) != [1, 1, 2, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6]:print( "seriesUp(6) not [1, 1, 2, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6]")

'''
maxMirror
We'll say that a "mirror" section in an array is a group of contiguous elements such that somewhere in the array, 
the same group appears in reverse order. For example, the largest mirror section in {1, 2, 3, 8, 9, 3, 2, 1} is length 3 
(the {1, 2, 3} part). Return the size of the largest mirror section found in the given array.
'''

# def maxMirror(nums):
#     if not nums or nums == []:
#         return 0
    
#     # create a mirror to compare against
#     mirror_nums = nums[::-1]
#     max_counter = 0
#     # print(mirror_nums)
#     # seek = [1,2,3]
#     for o in range(len(nums)):
#         seek = nums[0:o]
#         counter = 0
#         for i in range(len(nums) - len(seek)+1):
#             # print(mirror_nums[i:i + len(seek)])
#             if seek == mirror_nums[i:i + len(seek)]:
#                 counter = len(seek)
#                 print("hit " + str(seek))
#             if(max_counter < counter):
#                 max_counter = counter

#     print(max_counter)

'''
maxMirror
We'll say that a "mirror" section in an array is a group of contiguous elements such that somewhere in the array, 
the same group appears in reverse order. For example, the largest mirror section in {1, 2, 3, 8, 9, 3, 2, 1} is length 3 
(the {1, 2, 3} part). Return the size of the largest mirror section found in the given array.
'''

def maxMirror(nums):
    if not nums or nums == []:
        return 0 

    def is_listA_in_listB(a, b):
        for i in range(len(b)):
            if a == b[i:i + len(a)]:
                return True
        return False

    # create a mirror to compare against
    mirror_nums = nums[::-1]
    max_counter = 0
    for o in range(len(nums) + 1):
        for i in range(len(nums) + 1):
            if is_listA_in_listB(nums[o:i], mirror_nums) == True:
                if max_counter < len(nums[o:i]):
                    max_counter = len(nums[o:i])
    return max_counter

# if maxMirror([1, 2, 3, 8, 9, 3, 2, 1]) != 3:print("maxMirror([1, 2, 3, 8, 9, 3, 2, 1]) not 3")
# if maxMirror([1, 2, 1, 4]) != 3: print("maxMirror([1, 2, 1, 4]) not 3")
# if maxMirror([7, 1, 2, 9, 7, 2, 1]) != 2: print("maxMirror([7, 1, 2, 9, 7, 2, 1]) not 2")
# if maxMirror([21, 22, 9, 8, 7, 6, 23, 24, 6, 7, 8, 9, 25, 7, 8, 9]) != 4: print("maxMirror([21, 22, 9, 8, 7, 6, 23, 24, 6, 7, 8, 9, 25, 7, 8, 9]) not 4")
# if maxMirror([1, 2, 1, 20, 21, 1, 2, 1, 2, 23, 24, 2, 1, 2, 1, 25]) != 4: print("maxMirror([1, 2, 1, 20, 21, 1, 2, 1, 2, 23, 24, 2, 1, 2, 1, 25]) not 4")
# if maxMirror([1, 2, 3, 2, 1]) != 5: print("maxMirror([1, 2, 3, 2, 1]) not 5")
# if maxMirror([1, 2, 3, 3, 8]) != 2: print("maxMirror([1, 2, 3, 3, 8]) not 2")
# if maxMirror([1, 2, 7, 8, 1, 7, 2]) != 2: print("maxMirror([1, 2, 7, 8, 1, 7, 2]) not 2")
# if maxMirror([1, 1, 1]) != 3: print("maxMirror([1, 1, 1]) not 3")
# if maxMirror([1]) != 1: print("maxMirror([1]) not 1")
# if maxMirror([]) != 0: print("maxMirror([]) not 0")
# if maxMirror([9, 1, 1, 4, 2, 1, 1, 1]) != 3: print("maxMirror([9, 1, 1, 4, 2, 1, 1, 1]) not 3")
# if maxMirror([5, 9, 9, 4, 5, 4, 9, 9, 2]) != 7: print("maxMirror([5, 9, 9, 4, 5, 4, 9, 9, 2]) not 7")
# if maxMirror([5, 9, 9, 6, 5, 4, 9, 9, 2]) != 2: print("maxMirror([5, 9, 9, 6, 5, 4, 9, 9, 2]) nor 2")
# if maxMirror([5, 9, 1, 6, 5, 4, 1, 9, 5]) != 3: print("maxMirror([5, 9, 1, 6, 5, 4, 1, 9, 5]) not 3")

'''
countClumps
Say that a "clump" in an array is a series of 2 or more adjacent elements of the same value. 
Return the number of clumps in the given array.
'''

def countClumps(nums):
    counter = 0
    flag = 0
    # print(len(nums))
    for i in range(len(nums) -1 ):
        # print(i)
        # print("i is {} and loop length is {}".format(i, len(nums) -2))
        if nums[i] == nums[(i+1)]:
            flag = 1
        if nums[i] != nums[(i+1)] and flag == 1:
            # print(nums[i-1:i+2])
            flag = 0
            counter += 1
        if i == (len(nums) - 2) and flag == 1:
            # print(i)
            counter += 1
    return counter


# if countClumps([1, 2, 2, 3, 4, 4]) != 2: print("countClumps([1, 2, 2, 3, 4, 4]) not 2")
# if countClumps([1, 1, 2, 1, 1]) != 2: print("countClumps([1, 1, 2, 1, 1]) not 2")
# if countClumps([1, 1, 1, 1, 1]) != 1: print("countClumps([1, 1, 1, 1, 1]) not 1")
# if countClumps([1, 2, 3]) != 0: print("countClumps([1, 2, 3]) not 0")
# if countClumps([2, 2, 1, 1, 1, 2, 1, 1, 2, 2]) != 4: print("countClumps([2, 2, 1, 1, 1, 2, 1, 1, 2, 2]) not 4")
# if countClumps([0, 2, 2, 1, 1, 1, 2, 1, 1, 2, 2]) != 4: print("countClumps([0, 2, 2, 1, 1, 1, 2, 1, 1, 2, 2]) not 4")
# if countClumps([0, 0, 2, 2, 1, 1, 1, 2, 1, 1, 2, 2]) != 5: print("countClumps([0, 0, 2, 2, 1, 1, 1, 2, 1, 1, 2, 2]) not 5")
# if countClumps([0, 0, 0, 2, 2, 1, 1, 1, 2, 1, 1, 2, 2]) != 5: print("countClumps([0, 0, 0, 2, 2, 1, 1, 1, 2, 1, 1, 2, 2]) not 5")
