# these are problems at codingbat.com for java, testing them out on python

'''
scoresIncreasing 
Given an array of scores, return true if each score is equal or greater than the one before. The array will be length 2 or more.
'''
def scoresIncreasing(arr):
    for o in range(len(arr)):
        if o > 0 and arr[o] < arr[o-1]:
            return False
    return True


# if scoresIncreasing([1, 3, 4]) != True: print('scoresIncreasing([1, 3, 4])  not True')
# if scoresIncreasing([1, 3, 2]) != False: print('scoresIncreasing([1, 3, 2])  not False')
# if scoresIncreasing([1, 1, 4]) != True: print('scoresIncreasing([1, 1, 4])  not True')
# if scoresIncreasing([1, 1, 2, 4, 4, 7]) != True: print('scoresIncreasing([1, 1, 2, 4, 4, 7])  not True')
# if scoresIncreasing([1, 1, 2, 4, 3, 7]) != False: print('scoresIncreasing([1, 1, 2, 4, 3, 7])  not False')
# if scoresIncreasing([-5, 4, 11]) != True: print('scoresIncreasing([-5, 4, 11])  not True')

'''
scores100
Given an array of scores, return true if there are scores of 100 next to each other in the array. The array length will be at least 2.
'''

def scores100(arr):
    for o in range(len(arr)):
        if o > 0 and arr[o] == 100 and arr[o-1] == 100:
            return True
    return False


# if scores100([1, 100, 100]) != True: print('scores100([1, 100, 100])  not True')
# if scores100([1, 100, 99, 100]) != False: print('scores100([1, 100, 99, 100])  not False')
# if scores100([100, 1, 100, 100]) != True: print('scores100([100, 1, 100, 100])  not True')
# if scores100([100, 1, 100, 1]) != False: print('scores100([100, 1, 100, 1])  not False')
# if scores100([1, 2, 3, 4, 5]) != False: print('scores100([1, 2, 3, 4, 5])  not False')
# if scores100([1, 2, 100, 4, 5]) != False: print('scores100([1, 2, 100, 4, 5])  not False')

'''
scoresClump
Given an array of scores sorted in increasing order, return true if the array contains 3 adjacent scores that differ from each 
other by at most 2, such as with {3, 4, 5} or {3, 5, 5}.
'''

def scoresClump(arr):
    for o in range(len(arr)):
        if o > 1 and arr[o-2] <= arr[o-1] <= arr[o] and (arr[o] - arr[o-2]) <= 2:
            return True
    return False


# if scoresClump([3, 4, 5]) != True: print('scoresClump([3, 4, 5])  not True')
# if scoresClump([3, 4, 6]) != False: print('scoresClump([3, 4, 6])  not False')
# if scoresClump([1, 3, 5, 5]) != True: print('scoresClump([1, 3, 5, 5])  not True')
# if scoresClump([2, 4, 5, 6]) != True: print('scoresClump([2, 4, 5, 6])  not True')
# if scoresClump([2, 4, 5, 7]) != False: print('scoresClump([2, 4, 5, 7])  not False')
# if scoresClump([2, 4, 4, 7]) != True: print('scoresClump([2, 4, 4, 7])  not True')
# if scoresClump([3, 3, 6, 7, 9]) != False: print('scoresClump([3, 3, 6, 7, 9])  not False')
# if scoresClump([3, 3, 7, 7, 9]) != True: print('scoresClump([3, 3, 7, 7, 9])  not True')
# if scoresClump([4, 5, 8]) != False: print('scoresClump([4, 5, 8])  not False')

'''
scoresAverage
Given an array of scores, compute the int average of the first half and the second half, and return whichever is larger. 
We'll say that the second half begins at index length/2. The array length will be at least 2. To practice decomposition, 
write a separate helper method 
int average(int[] scores, int start, int end) { which computes the average of the elements between indexes start..end. 
Call your helper method twice to implement scoresAverage(). Write your helper method after your scoresAverage() method 
in the JavaBat text area. Normally you would compute averages with doubles, but here we use ints so the expected results are exact.
'''

def scoresAverage(arr):
    def average(arr, start, end):
        new_arr = []
        for o in range(start, end):
            new_arr += [arr[o]]
        return sum(new_arr) // (end - start)
    if len(arr) < 2:
        return arr
    if average(arr, 0, len(arr)//2) > average(arr, len(arr)//2, len(arr)):
        return average(arr, 0, len(arr)//2)
    return average(arr, len(arr)//2, len(arr))


# if scoresAverage([2, 2, 4, 4]) != 4: print('scoresAverage([2, 2, 4, 4])  not 4')
# if scoresAverage([4, 4, 4, 2, 2, 2]) != 4: print('scoresAverage([4, 4, 4, 2, 2, 2])  not 4')
# if scoresAverage([3, 4, 5, 1, 2, 3]) != 4: print('scoresAverage([3, 4, 5, 1, 2, 3])  not 4')
# if scoresAverage([5, 6]) != 6: print('scoresAverage([5, 6])  not 6')
# if scoresAverage([5, 4]) != 5: print('scoresAverage([5, 4])  not 5')
# if scoresAverage([5, 4, 5, 6, 2, 1, 2, 3]) != 5: print('scoresAverage([5, 4, 5, 6, 2, 1, 2, 3])  not 5')

'''
wordsCount
Given an array of strings, return the count of the number of strings with the given length.
'''

def wordsCount(arr,num):
    counter = 0 
    for o in range(len(arr)):
        if len(arr[o]) == num:
            counter += 1
    return counter


# if wordsCount(["a", "bb", "b", "ccc"], 1) != 2: print('wordsCount(["a", "bb", "b", "ccc"], 1)  not 2')
# if wordsCount(["a", "bb", "b", "ccc"], 3) != 1: print('wordsCount(["a", "bb", "b", "ccc"], 3)  not 1')
# if wordsCount(["a", "bb", "b", "ccc"], 4) != 0: print('wordsCount(["a", "bb", "b", "ccc"], 4)  not 0')
# if wordsCount(["xx", "yyy", "x", "yy", "z"], 1) != 2: print('wordsCount(["xx", "yyy", "x", "yy", "z"], 1)  not 2')
# if wordsCount(["xx", "yyy", "x", "yy", "z"], 2) != 2: print('wordsCount(["xx", "yyy", "x", "yy", "z"], 2)  not 2')
# if wordsCount(["xx", "yyy", "x", "yy", "z"], 3) != 1: print('wordsCount(["xx", "yyy", "x", "yy", "z"], 3)  not 1')

'''
wordsFront
Given an array of strings, return a new array containing the first N strings. N will be in the range 1..length.
'''

def wordsFront(arr,num):
    return arr[:num]


# if wordsFront(["a", "b", "c", "d"], 1) != ["a"]: print('wordsFront(["a", "b", "c", "d"], 1) not ["a"]')
# if wordsFront(["a", "b", "c", "d"], 2) != ["a", "b"]: print('wordsFront(["a", "b", "c", "d"], 2) not ["a", "b"]')
# if wordsFront(["a", "b", "c", "d"], 3) != ["a", "b", "c"]: print('wordsFront(["a", "b", "c", "d"], 3) not ["a", "b", "c"]')
# if wordsFront(["a", "b", "c", "d"], 4) != ["a", "b", "c", "d"]: print('wordsFront(["a", "b", "c", "d"], 4) not ["a", "b", "c", "d"]')
# if wordsFront(["Hi", "There"], 1) != ["Hi"]: print('wordsFront(["Hi", "There"], 1)  not ["Hi"]')
# if wordsFront(["Hi", "There"], 2) != ["Hi", "There"]: print('["Hi", "There"] not ["Hi", "There"]')

'''
wordsWithoutList
Given an array of strings, return a new List (e.g. an ArrayList) where all the strings of the given length are omitted. 
See wordsWithout() below which is more difficult because it uses arrays.
'''

# the hard way
def wordsWithoutList(arr, num):
    # gather the removables to a list of indexes
    remove_list = []
    for o in range(len(arr)):
        if len(arr[o]) == num:
            remove_list += [o]
    # reverse the list to be removed
    remove_list = remove_list[::-1]
    # remove the items from the array
    for o in range(len(remove_list)):
        print(o)
        del arr[remove_list[o]]
    return arr

# or the easy way
def wordsWithoutList(arr,num):
    result = []
    for o in range(len(arr)):
        if len(arr[o]) != num:
            result += [arr[o]]
    return result


# if wordsWithoutList(["a", "bb", "b", "ccc"], 1) != ["bb", "ccc"]: print('wordsWithoutList(["a", "bb", "b", "ccc"], 1) not ["bb", "ccc"]')
# if wordsWithoutList(["a", "bb", "b", "ccc"], 3) != ["a", "bb", "b"]: print('wordsWithoutList(["a", "bb", "b", "ccc"], 3) not ["a", "bb", "b"]')
# if wordsWithoutList(["a", "bb", "b", "ccc"], 4) != ["a", "bb", "b", "ccc"]: print('wordsWithoutList(["a", "bb", "b", "ccc"], 4)  not ["a", "bb", "b", "ccc"]')
# if wordsWithoutList(["xx", "yyy", "x", "yy", "z"], 1) != ["xx", "yyy", "yy"]: print('wordsWithoutList(["xx", "yyy", "x", "yy", "z"], 1) not ["xx", "yyy", "yy"]')
# if wordsWithoutList(["xx", "yyy", "x", "yy", "z"], 2) != ["yyy", "x", "z"]: print('wordsWithoutList(["xx", "yyy", "x", "yy", "z"], 2) not ["yyy", "x", "z"]')

'''
hasOne
Given a positive int n, return true if it contains a 1 digit. Note: use % to get the rightmost digit, and / to discard the 
rightmost digit.
'''

# find the answer by stringing
# def hasOne(num):
#     num = str(num)
#     for o in range(len(num)):
#         if num[o] == "1":
#             return True
#     return False

# find the answer by calculating
def hasOne(num):
    while num > 0:
        if num % 10 == 1:
            return True
        num = num // 10
    return False


# if hasOne(10) != True: print('hasOne(10)  not True')
# if hasOne(22) != False: print('hasOne(22)  not False')
# if hasOne(220) != False: print('hasOne(220)  not False')
# if hasOne(212) != True: print('hasOne(212)  not True')
# if hasOne(1) != True: print('hasOne(1)  not True')
# if hasOne(9) != False: print('hasOne(9)  not False')
# if hasOne(211112) != True: print('hasOne(211112)  not True')
# if hasOne(121121) != True: print('hasOne(121121)  not True')
# if hasOne(222222) != False: print('hasOne(222222)  not False')
# if hasOne(56156) != True: print('hasOne(56156)  not True')
# if hasOne(56556) != False: print('hasOne(56556)  not False')

'''
dividesSelf
We'll say that a positive int divides itself if every digit in the number divides into the number evenly. 
So for example 128 divides itself since 1, 2, and 8 all divide into 128 evenly. We'll say that 0 does not 
divide into anything evenly, so no number with a 0 digit divides itself. Note: use % to get the rightmost 
digit, and / to discard the rightmost digit.
'''

def dividesSelf(num):
    orig_num = num # so that we can test the mod against the original number
    while num > 0:
        dividend = num % 10
        if dividend == 0:
            return False
        elif orig_num % dividend != 0:
            return False
        num = num // 10
    return True


# if dividesSelf(128) != True: print('dividesSelf(128) not True')
# if dividesSelf(12) != True: print('dividesSelf(12) not True')
# if dividesSelf(120) != False: print('dividesSelf(120) not False')
# if dividesSelf(122) != True: print('dividesSelf(122) not True')
# if dividesSelf(13) != False: print('dividesSelf(13) not False')
# if dividesSelf(32) != False: print('dividesSelf(32) not False')
# if dividesSelf(22) != True: print('dividesSelf(22) not True')
# if dividesSelf(42) != False: print('dividesSelf(42) not False')
# if dividesSelf(212) != True: print('dividesSelf(212) not True')
# if dividesSelf(213) != False: print('dividesSelf(213) not False')
# if dividesSelf(162) != True: print('dividesSelf(162) not True')

'''
copyEvens
Given an array of positive ints, return a new array of length "count" containing the first even numbers from the original array. The original array will contain at least "count" even numbers.
'''

def copyEvens(arr,num):
    hit_counter = 0
    result = []
    for o in range(len(arr)):
        if arr[o] % 2 == 0:
            result += [arr[o]]
            hit_counter += 1
        if hit_counter == num:
            return result
    return result


# if copyEvens([3, 2, 4, 5, 8], 2) != [2, 4]: print('copyEvens([3, 2, 4, 5, 8], 2)  not  [2, 4]')
# if copyEvens([3, 2, 4, 5, 8], 3) != [2, 4, 8]: print('copyEvens([3, 2, 4, 5, 8], 3)  not  [2, 4, 8]')
# if copyEvens([6, 1, 2, 4, 5, 8], 3) != [6, 2, 4]: print('copyEvens([6, 1, 2, 4, 5, 8], 3)  not  [6, 2, 4]')
# if copyEvens([6, 1, 2, 4, 5, 8], 4) != [6, 2, 4, 8]: print('copyEvens([6, 1, 2, 4, 5, 8], 4)  not  [6, 2, 4, 8]')
# if copyEvens([3, 1, 4, 1, 5], 1) != [4]: print('copyEvens([3, 1, 4, 1, 5], 1)  not  [4]')
# if copyEvens([2], 1) != [2]: print('copyEvens([2], 1)  not  [2]')
# if copyEvens([6, 2, 4, 8], 2) != [6, 2]: print('copyEvens([6, 2, 4, 8], 2)  not  [6, 2]')
# if copyEvens([6, 2, 4, 8], 3) != [6, 2, 4]: print('copyEvens([6, 2, 4, 8], 3)  not  [6, 2, 4]')
# if copyEvens([6, 2, 4, 8], 4) != [6, 2, 4, 8]: print('copyEvens([6, 2, 4, 8], 4)  not  [6, 2, 4, 8]')
# if copyEvens([1, 8, 4], 1) != [8]: print('copyEvens([1, 8, 4], 1)  not  [8]')
# if copyEvens([1, 8, 4], 2) != [8, 4]: print('copyEvens([1, 8, 4], 2)  not  [8, 4]')
# if copyEvens([2, 8, 4], 2) != [2, 8]: print('copyEvens([2, 8, 4], 2)  not  [2, 8]')

'''
copyEndy
We'll say that a positive int n is "endy" if it is in the range 0..10 or 90..100 (inclusive). Given an array of positive ints, 
return a new array of length "count" containing the first endy numbers from the original array. Decompose out a separate isEndy(int n) 
method to test if a number is endy. The original array will contain at least "count" endy numbers.
'''

def copyEndy(arr,num):
    def is_endy(num):
        if num >= 0 and num <= 10 or num >= 90 and num <= 100:
            return True
        return False
    hit_counter = 0
    result = []
    for o in range(len(arr)):
        if is_endy(arr[o]) == True:
            result += [arr[o]]
            hit_counter += 1
        if hit_counter == num:
            return result
    return result


# if copyEndy([9, 11, 90, 22, 6], 2) != [9, 90]: print('copyEndy([9, 11, 90, 22, 6], 2)  not  [9, 90]')
# if copyEndy([9, 11, 90, 22, 6], 3) != [9, 90, 6]: print('copyEndy([9, 11, 90, 22, 6], 3)  not  [9, 90, 6]')
# if copyEndy([12, 1, 1, 13, 0, 20], 2) != [1, 1]: print('copyEndy([12, 1, 1, 13, 0, 20], 2)  not  [1, 1]')
# if copyEndy([12, 1, 1, 13, 0, 20], 3) != [1, 1, 0]: print('copyEndy([12, 1, 1, 13, 0, 20], 3)  not  [1, 1, 0]')
# if copyEndy([0], 1) != [0]: print('copyEndy([0], 1)  not  [0]')
# if copyEndy([10, 11, 90], 2) != [10, 90]: print('copyEndy([10, 11, 90], 2)  not  [10, 90]')
# if copyEndy([90, 22, 100], 2) != [90, 100]: print('copyEndy([90, 22, 100], 2)  not  [90, 100]')
# if copyEndy([12, 11, 10, 89, 101, 4], 1) != [10]: print('copyEndy([12, 11, 10, 89, 101, 4], 1)  not  [10]')
# if copyEndy([13, 2, 2, 0], 2) != [2, 2]: print('copyEndy([13, 2, 2, 0], 2)  not  [2, 2]')
# if copyEndy([13, 2, 2, 0], 3) != [2, 2, 0]: print('copyEndy([13, 2, 2, 0], 3)  not  [2, 2, 0]')
# if copyEndy([13, 2, 13, 2, 0, 30], 2) != [2, 2]: print('copyEndy([13, 2, 13, 2, 0, 30], 2)  not  [2, 2]')
# if copyEndy([13, 2, 13, 2, 0, 30], 3) != [2, 2, 0]: print('copyEndy([13, 2, 13, 2, 0, 30], 3)  not  [2, 2, 0]')

'''
matchUp
Given 2 arrays that are the same length containing strings, compare the 1st string in one array to the 1st string in the other array, 
the 2nd to the 2nd and so on. Count the number of times that the 2 strings are non-empty and start with the same char. 
The strings may be any length, including 0.
'''

def matchUp(arr1,arr2):
    counter = 0
    for o in range(len(arr1)):
        try:
            if arr1[o][0] == arr2[o][0]:
                counter += 1
        except IndexError:
            pass
    return counter


# if matchUp(["aa", "bb", "cc"], ["", "", "ccc"]) != 1: print('matchUp(["aa", "bb", "cc"], ["", "", "ccc"])  not 1')
# if matchUp(["", "", "ccc"], ["aa", "bb", "cc"]) != 1: print('matchUp(["", "", "ccc"], ["aa", "bb", "cc"])  not 1')
# if matchUp(["", "", ""], ["", "bb", "cc"]) != 0: print('matchUp(["", "", ""], ["", "bb", "cc"])  not 0')
# if matchUp(["aa", "bb", "cc"], ["", "", ""]) != 0: print('matchUp(["aa", "bb", "cc"], ["", "", ""])  not 0')
# if matchUp(["aa", "", "ccc"], ["", "bb", "cc"]) != 1: print('matchUp(["aa", "", "ccc"], ["", "bb", "cc"])  not 1')
# if matchUp(["x", "y", "z"], ["y", "z", "x"]) != 0: print('matchUp(["x", "y", "z"], ["y", "z", "x"])  not 0')
# if matchUp(["", "y", "z"], ["", "y", "x"]) != 1: print('matchUp(["", "y", "z"], ["", "y", "x"])  not 1')
# if matchUp(["x", "y", "z"], ["xx", "yyy", "zzz"]) != 3: print('matchUp(["x", "y", "z"], ["xx", "yyy", "zzz"])  not 3')
# if matchUp(["x", "y", "z"], ["xx", "yyy", ""]) != 2: print('matchUp(["x", "y", "z"], ["xx", "yyy", ""])  not 2')
# if matchUp(["b", "x", "y", "z"], ["a", "xx", "yyy", "zzz"]) != 3: print('matchUp(["b", "x", "y", "z"], ["a", "xx", "yyy", "zzz"])  not 3')
# if matchUp(["aaa", "bb", "c"], ["aaa", "xx", "bb"]) != 1: print('matchUp(["aaa", "bb", "c"], ["aaa", "xx", "bb"])  not 1')

'''
scoreUp
The "key" array is an array containing the correct answers to an exam, like {"a", "a", "b", "b"}. the "answers" 
array contains a student's answers, with "?" representing a question left blank. The two arrays are not empty and 
are the same length. Return the score for this array of answers, giving +4 for each correct answer, -1 for each 
incorrect answer, and +0 for each blank answer.
'''
def scoreUp(a,b):
    counter = 0
    for o in range(len(a)):
        # print(a[o], " and ", b[o])
        if a[o] == b[o]:
            # print('+4')
            counter += 4
        elif b[o] == "?":
            # print("+0")
            counter += 0
        elif a[o] != b[o]:
            # print("-1")
            counter += -1
    return counter


# if scoreUp(["a", "a", "b", "b"], ["a", "c", "b", "c"]) != 6: print('scoreUp(["a", "a", "b", "b"], ["a", "c", "b", "c"])  not 6')
# if scoreUp(["a", "a", "b", "b"], ["a", "a", "b", "c"]) != 11: print('scoreUp(["a", "a", "b", "b"], ["a", "a", "b", "c"])  not 11')
# if scoreUp(["a", "a", "b", "b"], ["a", "a", "b", "b"]) != 16: print('scoreUp(["a", "a", "b", "b"], ["a", "a", "b", "b"])  not 16')
# if scoreUp(["a", "a", "b", "b"], ["?", "c", "b", "?"]) != 3: print('scoreUp(["a", "a", "b", "b"], ["?", "c", "b", "?"])  not 3')
# if scoreUp(["a", "a", "b", "b"], ["?", "c", "?", "?"]) != -1: print('scoreUp(["a", "a", "b", "b"], ["?", "c", "?", "?"])  not -1')
# if scoreUp(["a", "a", "b", "b"], ["c", "?", "b", "b"]) != 7: print('scoreUp(["a", "a", "b", "b"], ["c", "?", "b", "b"])  not 7')
# if scoreUp(["a", "a", "b", "b"], ["c", "?", "b", "?"]) != 3: print('scoreUp(["a", "a", "b", "b"], ["c", "?", "b", "?"])  not 3')
# if scoreUp(["a", "b", "c"], ["a", "c", "b"]) != 2: print('scoreUp(["a", "b", "c"], ["a", "c", "b"])  not 2')
# if scoreUp(["a", "a", "b", "b", "c", "c"], ["a", "c", "a", "c", "a", "c"]) != 4: print('scoreUp(["a", "a", "b", "b", "c", "c"], ["a", "c", "a", "c", "a", "c"])  not 4')
# if scoreUp(["a", "a", "b", "b", "c", "c"], ["a", "c", "?", "?", "a", "c"]) != 6: print('scoreUp(["a", "a", "b", "b", "c", "c"], ["a", "c", "?", "?", "a", "c"])  not 6')
# if scoreUp(["a", "a", "b", "b", "c", "c"], ["a", "c", "?", "?", "c", "c"]) != 11: print('scoreUp(["a", "a", "b", "b", "c", "c"], ["a", "c", "?", "?", "c", "c"])  not 11')
# if scoreUp(["a", "b", "c"], ["a", "b", "c"]) != 12: print('scoreUp(["a", "b", "c"], ["a", "b", "c"])  not 12')

'''
wordsWithout
Given an array of strings, return a new array without the strings that are equal to the target string. One approach is 
to count the occurrences of the target string, make a new array of the correct length, and then copy over the correct strings.
'''
def wordsWithout(arr,letter):
    result = []
    for o in range(len(arr)):
        if arr[o] != letter:
            result += [arr[o]]
    return result


# if wordsWithout(["a", "b", "c", "a"], "a") != ["b", "c"]: print('wordsWithout(["a", "b", "c", "a"], "a")  not  ["b", "c"]')
# if wordsWithout(["a", "b", "c", "a"], "b") != ["a", "c", "a"]: print('wordsWithout(["a", "b", "c", "a"], "b")  not  ["a", "c", "a"]')
# if wordsWithout(["a", "b", "c", "a"], "c") != ["a", "b", "a"]: print('wordsWithout(["a", "b", "c", "a"], "c")  not  ["a", "b", "a"]')
# if wordsWithout(["b", "c", "a", "a"], "b") != ["c", "a", "a"]: print('wordsWithout(["b", "c", "a", "a"], "b")  not  ["c", "a", "a"]')
# if wordsWithout(["xx", "yyy", "x", "yy", "x"], "x") != ["xx", "yyy", "yy"]: print( 'wordsWithout(["xx", "yyy", "x", "yy", "x"], "x")  not  ["xx", "yyy", "yy"]')
# if wordsWithout(["xx", "yyy", "x", "yy", "x"], "yy") != ["xx", "yyy", "x", "x"]: print( 'wordsWithout(["xx", "yyy", "x", "yy", "x"], "yy")  not  ["xx", "yyy", "x", "x"]')
# if wordsWithout(["aa", "ab", "ac", "aa"], "aa") != ["ab", "ac"]: print('wordsWithout(["aa", "ab", "ac", "aa"], "aa")  not  ["ab", "ac"]')

'''
scoresSpecial
Given two arrays, A and B, of non-negative int scores. A "special" score is one which is a multiple of 10, such as 40 or 90. 
Return the sum of largest special score in A and the largest special score in B. To practice decomposition, write a separate
helper method which finds the largest special score in an array. Write your helper method after your scoresSpecial() method
in the JavaBat text area.
'''
def scoresSpecial(a,b):
    def seek_highest_mod_10(a):
        high_score = 0
        for o in range(len(a)):
            if a[o] % 10 == 0:
                if a[o] > high_score:
                    high_score = a[o]
        return high_score
    return seek_highest_mod_10(a) + seek_highest_mod_10(b)


# if scoresSpecial([12, 10, 4], [2, 20, 30]) != 40: print('scoresSpecial([12, 10, 4], [2, 20, 30])  not 40')
# if scoresSpecial([20, 10, 4], [2, 20, 10]) != 40: print('scoresSpecial([20, 10, 4], [2, 20, 10])  not 40')
# if scoresSpecial([12, 11, 4], [2, 20, 31]) != 20: print('scoresSpecial([12, 11, 4], [2, 20, 31])  not 20')
# if scoresSpecial([1, 20, 2, 50], [3, 4, 5]) != 50: print('scoresSpecial([1, 20, 2, 50], [3, 4, 5])  not 50')
# if scoresSpecial([3, 4, 5], [1, 50, 2, 20]) != 50: print('scoresSpecial([3, 4, 5], [1, 50, 2, 20])  not 50')
# if scoresSpecial([10, 4, 20, 30], [20]) != 50: print('scoresSpecial([10, 4, 20, 30], [20])  not 50')
# if scoresSpecial([10, 4, 20, 30], [20]) != 50: print('scoresSpecial([10, 4, 20, 30], [20])  not 50')
# if scoresSpecial([10, 4, 20, 30], [3, 20, 99]) != 50: print('scoresSpecial([10, 4, 20, 30], [3, 20, 99])  not 50')
# if scoresSpecial([10, 4, 20, 30], [30, 20, 99]) != 60: print('scoresSpecial([10, 4, 20, 30], [30, 20, 99])  not 60')
# if scoresSpecial([], [2]) != 0: print('scoresSpecial([], [2])  not 0')
# if scoresSpecial([], [20]) != 20: print('scoresSpecial([], [20])  not 20')
# if scoresSpecial([14, 10, 4], [4, 20, 30]) != 40: print('scoresSpecial([14, 10, 4], [4, 20, 30])  not 40')

'''
sumHeights
We have an array of heights, representing the altitude along a walking trail. Given start/end indexes into the array, 
return the sum of the changes for a walk beginning at the start index and ending at the end index. For example, with the 
heights {5, 3, 6, 7, 2} and start=2, end=4 yields a sum of 1 + 5 = 6. The start end end index will both be valid indexes 
into the array with start <= end.
'''

def sumHeights(arr,start,end):
    diff_sum = 0
    for o in range(start,end):
        # print("loop ", o, " array o ",arr[o], " array o+1", arr[o +1])
        # print(abs(arr[o] - arr[o+1]))
        diff_sum += abs(arr[o] - arr[o+1])
    return diff_sum


# if sumHeights([5, 3, 6, 7, 2], 2, 4) != 6: print('sumHeights([5, 3, 6, 7, 2], 2, 4)  not 6')
# if sumHeights([5, 3, 6, 7, 2], 0, 1) != 2: print('sumHeights([5, 3, 6, 7, 2], 0, 1)  not 2')
# if sumHeights([5, 3, 6, 7, 2], 0, 4) != 11: print('sumHeights([5, 3, 6, 7, 2], 0, 4)  not 11')
# if sumHeights([5, 3, 6, 7, 2], 1, 1) != 0: print('sumHeights([5, 3, 6, 7, 2], 1, 1)  not 0')
# if sumHeights([1, 2, 3, 4, 5, 4, 3, 2, 10], 0, 3) != 3: print('sumHeights([1, 2, 3, 4, 5, 4, 3, 2, 10], 0, 3)  not 3')
# if sumHeights([1, 2, 3, 4, 5, 4, 3, 2, 10], 4, 8) != 11: print('sumHeights([1, 2, 3, 4, 5, 4, 3, 2, 10], 4, 8)  not 11')
# if sumHeights([1, 2, 3, 4, 5, 4, 3, 2, 10], 7, 8) != 8: print('sumHeights([1, 2, 3, 4, 5, 4, 3, 2, 10], 7, 8)  not 8')
# if sumHeights([1, 2, 3, 4, 5, 4, 3, 2, 10], 8, 8) != 0: print('sumHeights([1, 2, 3, 4, 5, 4, 3, 2, 10], 8, 8)  not 0')
# if sumHeights([1, 2, 3, 4, 5, 4, 3, 2, 10], 2, 2) != 0: print('sumHeights([1, 2, 3, 4, 5, 4, 3, 2, 10], 2, 2)  not 0')
# if sumHeights([1, 2, 3, 4, 5, 4, 3, 2, 10], 3, 6) != 3: print('sumHeights([1, 2, 3, 4, 5, 4, 3, 2, 10], 3, 6)  not 3')
# if sumHeights([10, 8, 7, 7, 7, 6, 7], 1, 4) != 1: print('sumHeights([10, 8, 7, 7, 7, 6, 7], 1, 4)  not 1')
# if sumHeights([10, 8, 7, 7, 7, 6, 7], 1, 5) != 2: print('sumHeights([10, 8, 7, 7, 7, 6, 7], 1, 5)  not 2')

'''
sumHeights2
(A variation on the sumHeights problem.) We have an array of heights, representing the altitude along a walking trail. 
Given start/end indexes into the array, return the sum of the changes for a walk beginning at the start index and ending 
at the end index, however increases in height count double. For example, with the heights {5, 3, 6, 7, 2} and start=2, 
end=4 yields a sum of 1*2 + 5 = 7. The start end end index will both be valid indexes into the array with start <= end.
'''
def sumHeights2(arr,start,end):
    diff_sum = 0
    for o in range(start,end):
        diff_sum += abs(arr[o] - arr[o+1])
        if arr[o] < arr[o+1]:
            diff_sum += abs(arr[o] - arr[o+1])
    return diff_sum


# if sumHeights2([5, 3, 6, 7, 2], 2, 4) != 7: print('sumHeights2([5, 3, 6, 7, 2], 2, 4)  not 7')
# if sumHeights2([5, 3, 6, 7, 2], 0, 1) != 2: print('sumHeights2([5, 3, 6, 7, 2], 0, 1)  not 2')
# if sumHeights2([5, 3, 6, 7, 2], 0, 4) != 15: print('sumHeights2([5, 3, 6, 7, 2], 0, 4)  not 15')
# if sumHeights2([5, 3, 6, 7, 2], 1, 1) != 0: print('sumHeights2([5, 3, 6, 7, 2], 1, 1)  not 0')
# if sumHeights2([1, 2, 3, 4, 5, 4, 3, 2, 10], 0, 3) != 6: print('sumHeights2([1, 2, 3, 4, 5, 4, 3, 2, 10], 0, 3)  not 6')
# if sumHeights2([1, 2, 3, 4, 5, 4, 3, 2, 10], 4, 8) != 19: print('sumHeights2([1, 2, 3, 4, 5, 4, 3, 2, 10], 4, 8)  not 19')
# if sumHeights2([1, 2, 3, 4, 5, 4, 3, 2, 10], 7, 8) != 16: print('sumHeights2([1, 2, 3, 4, 5, 4, 3, 2, 10], 7, 8)  not 16')
# if sumHeights2([1, 2, 3, 4, 5, 4, 3, 2, 10], 8, 8) != 0: print('sumHeights2([1, 2, 3, 4, 5, 4, 3, 2, 10], 8, 8)  not 0')
# if sumHeights2([1, 2, 3, 4, 5, 4, 3, 2, 10], 2, 2) != 0: print('sumHeights2([1, 2, 3, 4, 5, 4, 3, 2, 10], 2, 2)  not 0')
# if sumHeights2([1, 2, 3, 4, 5, 4, 3, 2, 10], 3, 6) != 4: print('sumHeights2([1, 2, 3, 4, 5, 4, 3, 2, 10], 3, 6)  not 4')
# if sumHeights2([10, 8, 7, 7, 7, 6, 7], 1, 4) != 1: print('sumHeights2([10, 8, 7, 7, 7, 6, 7], 1, 4)  not 1')
# if sumHeights2([10, 8, 7, 7, 7, 6, 7], 1, 5) != 2: print('sumHeights2([10, 8, 7, 7, 7, 6, 7], 1, 5)  not 2')

'''
bigHeights
(A variation on the sumHeights problem.) We have an array of heights, representing the altitude along a walking trail. 
Given start/end indexes into the array, return the number of "big" steps for a walk starting at the start index and 
ending at the end index. We'll say that step is big if it is 5 or more up or down. The start end end index will both 
be valid indexes into the array with start <= end.
'''
def bigHeights(arr,start,stop):
    big_steps_counter = 0
    for o in range(start,stop):
        if abs(arr[o] - arr[o+1]) >= 5:
            big_steps_counter += 1
    return big_steps_counter


# if bigHeights([5, 3, 6, 7, 2], 2, 4) != 1: print('bigHeights([5, 3, 6, 7, 2], 2, 4)  not 1')
# if bigHeights([5, 3, 6, 7, 2], 0, 1) != 0: print('bigHeights([5, 3, 6, 7, 2], 0, 1)  not 0')
# if bigHeights([5, 3, 6, 7, 2], 0, 4) != 1: print('bigHeights([5, 3, 6, 7, 2], 0, 4)  not 1')
# if bigHeights([5, 3, 6, 7, 3], 0, 4) != 0: print('bigHeights([5, 3, 6, 7, 3], 0, 4)  not 0')
# if bigHeights([5, 3, 6, 7, 2], 1, 1) != 0: print('bigHeights([5, 3, 6, 7, 2], 1, 1)  not 0')
# if bigHeights([5, 13, 6, 7, 2], 1, 2) != 1: print('bigHeights([5, 13, 6, 7, 2], 1, 2)  not 1')
# if bigHeights([5, 13, 6, 7, 2], 0, 2) != 2: print('bigHeights([5, 13, 6, 7, 2], 0, 2)  not 2')
# if bigHeights([5, 13, 6, 7, 2], 1, 4) != 2: print('bigHeights([5, 13, 6, 7, 2], 1, 4)  not 2')
# if bigHeights([5, 13, 6, 7, 2], 0, 4) != 3: print('bigHeights([5, 13, 6, 7, 2], 0, 4)  not 3')
# if bigHeights([5, 13, 6, 7, 2], 0, 3) != 2: print('bigHeights([5, 13, 6, 7, 2], 0, 3)  not 2')
# if bigHeights([1, 2, 3, 4, 5, 4, 3, 2, 10], 0, 3) != 0: print('bigHeights([1, 2, 3, 4, 5, 4, 3, 2, 10], 0, 3)  not 0')
# if bigHeights([1, 2, 3, 4, 5, 4, 3, 2, 10], 4, 8) != 1: print('bigHeights([1, 2, 3, 4, 5, 4, 3, 2, 10], 4, 8)  not 1')
# if bigHeights([1, 2, 3, 14, 5, 4, 3, 2, 10], 0, 3) != 1: print('bigHeights([1, 2, 3, 14, 5, 4, 3, 2, 10], 0, 3)  not 1')
# if bigHeights([1, 2, 3, 14, 5, 4, 3, 2, 10], 7, 8) != 1: print('bigHeights([1, 2, 3, 14, 5, 4, 3, 2, 10], 7, 8)  not 1')
# if bigHeights([1, 2, 3, 14, 5, 4, 3, 2, 10], 3, 8) != 2: print('bigHeights([1, 2, 3, 14, 5, 4, 3, 2, 10], 3, 8)  not 2')
# if bigHeights([1, 2, 3, 14, 5, 4, 3, 2, 10], 2, 8) != 3: print('bigHeights([1, 2, 3, 14, 5, 4, 3, 2, 10], 2, 8)  not 3')

'''
userCompare
We have data for two users, A and B, each with a String name and an int id. The goal is to order the users such as for
sorting. Return -1 if A comes before B, 1 if A comes after B, and 0 if they are the same. Order first by the string names,
and then by the id numbers if the names are the same. Note: with Strings str1.compareTo(str2) returns an int value which 
is negative/0/positive to indicate how str1 is ordered to str2 (the value is not limited to -1/0/1). (On the AP, there 
would be two User objects, but here the code simply takes the two strings and two ints directly. The code logic is the 
same.)
'''
def userCompare(aName,aId,bName,bId):
    if aName > bName:
        return 1
    elif aName < bName:
        return -1
    elif aName == bName:
        if aId > bId:
            return 1
        elif aId < bId:
            return -1
    return 0


# if userCompare("bb", 1, "zz", 2) != -1: print('userCompare("bb", 1, "zz", 2)  not -1')
# if userCompare("bb", 1, "aa", 2) != 1: print('userCompare("bb", 1, "aa", 2)  not 1')
# if userCompare("bb", 1, "bb", 1) != 0: print('userCompare("bb", 1, "bb", 1)  not 0')
# if userCompare("bb", 5, "bb", 1) != 1: print('userCompare("bb", 5, "bb", 1)  not 1')
# if userCompare("bb", 5, "bb", 10) != -1: print('userCompare("bb", 5, "bb", 10)  not -1')
# if userCompare("adam", 1, "bob", 2) != -1: print('userCompare("adam", 1, "bob", 2)  not -1')
# if userCompare("bob", 1, "bob", 2) != -1: print('userCompare("bob", 1, "bob", 2)  not -1')
# if userCompare("bzb", 1, "bob", 2) != 1: print('userCompare("bzb", 1, "bob", 2)  not 1')

'''
mergeTwo
Start with two arrays of strings, A and B, each with its elements in alphabetical order and without duplicates. 
Return a new array containing the first N elements from the two arrays. The result array should be in alphabetical 
order and without duplicates. A and B will both have a length which is N or more. The best "linear" solution makes 
a single pass over A and B, taking advantage of the fact that they are in alphabetical order, copying elements directly 
to the new array.
'''
def mergeTwo(arr1,arr2,num):
    result = []
    arr1_loc = 0
    arr2_loc = 0
    for o in range(len(arr1)):
        # print("locations ", arr1_loc, " and ", arr2_loc)
        if len(result) == num:
            return result
        if arr1[arr1_loc] == arr2[arr2_loc]:
            result += arr1[arr1_loc]
            arr1_loc += 1
            arr2_loc += 1
        elif arr1[arr1_loc] < arr2[arr2_loc]:
            result += arr1[arr1_loc]
            arr1_loc += 1
        elif arr1[arr1_loc] > arr2[arr2_loc]:
            result += arr2[arr2_loc]
            arr2_loc += 1
    return result


# if mergeTwo(["a", "c", "z"], ["b", "f", "z"], 3) != ["a", "b", "c"]: print('mergeTwo(["a", "c", "z"], ["b", "f", "z"], 3)  not  ["a", "b", "c"]')
# if mergeTwo(["a", "c", "z"], ["c", "f", "z"], 3) != ["a", "c", "f"]: print('mergeTwo(["a", "c", "z"], ["c", "f", "z"], 3)  not  ["a", "c", "f"]')
# if mergeTwo(["f", "g", "z"], ["c", "f", "g"], 3) != ["c", "f", "g"]: print('mergeTwo(["f", "g", "z"], ["c", "f", "g"], 3)  not  ["c", "f", "g"]')
# if mergeTwo(["a", "c", "z"], ["a", "c", "z"], 3) != ["a", "c", "z"]: print('mergeTwo(["a", "c", "z"], ["a", "c", "z"], 3)  not  ["a", "c", "z"]')
# if mergeTwo(["a", "b", "c", "z"], ["a", "c", "z"], 3) != ["a", "b", "c"]: print('mergeTwo(["a", "b", "c", "z"], ["a", "c", "z"], 3)  not  ["a", "b", "c"]')
# if mergeTwo(["a", "c", "z"], ["a", "b", "c", "z"], 3) != ["a", "b", "c"]: print('mergeTwo(["a", "c", "z"], ["a", "b", "c", "z"], 3)  not  ["a", "b", "c"]')
# if mergeTwo(["a", "c", "z"], ["a", "c", "z"], 2) != ["a", "c"]: print('mergeTwo(["a", "c", "z"], ["a", "c", "z"], 2)  not  ["a", "c"]')
# if mergeTwo(["a", "c", "z"], ["a", "c", "y", "z"], 3) != ["a", "c", "y"]: print('mergeTwo(["a", "c", "z"], ["a", "c", "y", "z"], 3)  not  ["a", "c", "y"]')
# if mergeTwo(["x", "y", "z"], ["a", "b", "z"], 3) != ["a", "b", "x"]: print('mergeTwo(["x", "y", "z"], ["a", "b", "z"], 3)  not  ["a", "b", "x"]')

'''
commonTwo
Start with two arrays of strings, a and b, each in alphabetical order, possibly with duplicates. Return the count of 
the number of strings which appear in both arrays. The best "linear" solution makes a single pass over both arrays, 
taking advantage of the fact that they are in alphabetical order.
'''

def commonTwo(arr1,arr2):
    def unique_array_ordered(arr):
        return sorted(list(set(arr)))
    # first sort the arrays into unique values
    arr1 = unique_array_ordered(arr1)
    arr2 = unique_array_ordered(arr2)
    counter = 0
    # count the duplicates on the unique values listed from the shorter list
    if len(arr1) < len(arr2):
        for o in range(len(arr1)):
            if arr1[o] in arr2:
                counter += 1
    else:
        for o in range(len(arr2)):
            if arr2[o] in arr1:
                counter += 1
    return counter

if commonTwo(["a", "c", "x"], ["b", "c", "d", "x"])  != 2 :print('commonTwo(["a", "c", "x"], ["b", "c", "d", "x"])  not 2')
if commonTwo(["a", "c", "x"], ["a", "b", "c", "x", "z"])  != 3 :print('commonTwo(["a", "c", "x"], ["a", "b", "c", "x", "z"])  not 3')
if commonTwo(["a", "b", "c"], ["a", "b", "c"])  != 3 :print('commonTwo(["a", "b", "c"], ["a", "b", "c"])  not 3')
if commonTwo(["a", "a", "b", "b", "c"], ["a", "b", "c"])  != 3 :print('commonTwo(["a", "a", "b", "b", "c"], ["a", "b", "c"])  not 3')
if commonTwo(["a", "a", "b", "b", "c"], ["a", "b", "b", "b", "c"])  != 3 :print('commonTwo(["a", "a", "b", "b", "c"], ["a", "b", "b", "b", "c"])  not 3')
if commonTwo(["a", "a", "b", "b", "c"], ["a", "b", "b", "c", "c"])  != 3 :print('commonTwo(["a", "a", "b", "b", "c"], ["a", "b", "b", "c", "c"])  not 3')
if commonTwo(["b", "b", "b", "b", "c"], ["a", "b", "b", "b", "c"])  != 2 :print('commonTwo(["b", "b", "b", "b", "c"], ["a", "b", "b", "b", "c"])  not 2')
if commonTwo(["a", "b", "c", "c", "d"], ["a", "b", "b", "c", "d", "d"])  != 4 :print('commonTwo(["a", "b", "c", "c", "d"], ["a", "b", "b", "c", "d", "d"])  not 4')
if commonTwo(["a", "a", "b", "b", "c"], ["b", "b", "b"])  != 1 :print('commonTwo(["a", "a", "b", "b", "c"], ["b", "b", "b"])  not 1')
if commonTwo(["a", "a", "b", "b", "c"], ["c", "c"])  != 1 :print('commonTwo(["a", "a", "b", "b", "c"], ["c", "c"])  not 1')
if commonTwo(["a", "a", "b", "b", "c"], ["b", "b", "b", "x"])  != 1 :print('commonTwo(["a", "a", "b", "b", "c"], ["b", "b", "b", "x"])  not 1')
if commonTwo(["a", "a", "b", "b", "c"], ["b", "b"])  != 1 :print('commonTwo(["a", "a", "b", "b", "c"], ["b", "b"])  not 1')
