def string_times(str,n):
    if n > 0:
        new_str = ""
        for i in range(n):
            new_str += str
        return new_str
    else:
        return ""
# print(string_times("This",4))

def front_times(str,n):
    if n > 0:
        str = str[:3]
        new_str = ""
        for i in range(n):
            new_str += str
        return new_str
    else:
        return ""
# print(front_times("jIpp", 6))

def string_splosion(str):
    result = ""
    count = 0
    for i in str:
        count += 1
        result += str[:count]
    return result
# print(string_splosion("Elisa"))

def last2(str):
    search_str = str[-2:]
    hit_counter = 0
    for i in range(len(str) -2 ):
        if search_str == (str[i] + str[i + 1]):
            hit_counter += 1
    return hit_counter
# print(last2("13121311"))
# print(last2('xxaxxaxxaxx'))

def array_count9(nums):
    result = 0
    for i in nums:
        if i == 9:
            result += 1
    return result
# print(array_count9([1,2,9]))
# print(array_count9([1,9,9]))

def array_front9(nums):
    max_range = 0
    if len(nums) <= 4:
        max_range = len(nums)
    else:
        max_range = 4
    for i in range(0,max_range):
        if nums[i] == 9:
            return True
    return False
# print(array_front9([1,2,9,3,4]))
# print(array_front9([1,2,3,4,9]))
# print(array_front9([1,2,3,4,5]))
# print(array_front9([1,2,3]))
# print(array_front9([1,2,9]))
# print(array_front9([1,2]))
# print(array_front9([9, 2, 3]))

# # works as a counter
# def array123(nums):
#     counter = 0
#     for i in range(len(nums) - 2):
#         seqence = str(nums[i]) + str(nums[i + 1]) + str(nums[i + 2])
#         if seqence == "123":
#             counter += 1
#     return counter

def array123(nums):
    for i in range(len(nums) - 2):
        seqence = str(nums[i]) + str(nums[i + 1]) + str(nums[i + 2])
        if seqence == "123":
            return True
    return False
# print(array123([1, 1, 2, 3, 1]))
# print(array123([1, 1, 2, 4, 1]))
# print(array123([1, 1, 2, 1, 2, 3]))
# print(array123([1, 1, 2, 1, 2, 3, 1, 2, 1, 2, 3]))

# # Did the exercise with wrong goal, should read more carefully
# def string_match(a,b):
#     result = 0
#     if len(a) >= len(b):
#         max_range = len(b)
#     else:
#         max_range = len(a)
#     for i in range(max_range):
#         if a[i] == b[i]:
#             #print("matching values a {} and b {} with an index of {}".format(a[i],b[i],i))
#             result += 1
#     return result
# print(string_match('xxcaazz','xxbaaz'))

def string_match(a,b):
    result = 0
    if len(a) >= len(b):
        max_range = len(b)
    else:
        max_range = len(a)
    for i in range(max_range - 1):
        if (str(a[i]) + str(a[i + 1])) == (str(b[i]) + str(b[i + 1])):
            print("matching values a {} and b {} with an index of {}".format(a[i],b[i],i))
            result += 1
    return result
# print(string_match('xxcaazz','xxbaaz'))
