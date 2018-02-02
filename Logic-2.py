
# # 1'st attempt, its borken
# def make_bricks(small,big,goal):
#     big_size = 5
#     total_big = big * big_size
#     # print(total_big)
#     if total_big == goal:
#         return True
#     elif total_big > goal:
#         for i in range(big + 1):
#             print("!" + str(total_big - (i * big_size) + small))
#             if (total_big - (i * big_size) + small) == goal:
#                 return True
#             elif (total_big - (i * big_size) + small) > goal:
#                 for s in range(small,0,-1):
#                     # print(str(total_big - (i * big_size) + s) + "!")
#                     # print(str(total_big - (i * big_size)) + "!!")
#                     print(str(s) + "!!!")
#                     print( "!!" + str(total_big - (i * big_size) + s))
#                     if (total_big - (i * big_size) + s) == goal:
#                         return True
#                     elif s == 0:
#                         return False
#             elif (total_big - (i * big) + small) < goal:
#                 return False
#     elif (total_big + small) >= goal:
#         return True
#     else:
#         return False

# # Works, but times out on codingbat due to the loop restriction
# def make_bricks(small,big,goal):
#     big_size = 5
#     small_size = 1
#     total_big = big * big_size
#     total_small = small * small_size
#     if total_big + total_small == goal:
#         return True
#     elif total_big + total_small < goal:
#         return False
#     else:
#         for b in reversed(range(big + 1)):
#             # print(b * big_size)
#             if b * big_size == goal:
#                 return True
#             elif b * big_size < goal:
#                 for s in reversed(range(small + 1)):
#                     # print(b,s)
#                     # print((small_size * s) + (b * big_size))
#                     if (s * small_size) + (b * big_size) == goal:
#                         return True
#         return False

# # First attempt with mod use
def make_bricks(small,big,goal):
    total_big = big * 5
    if total_big + small == goal:
        return True
    elif total_big + small > goal:
        if total_big > goal:
            if goal % 5 <= small:
                return True
            else:
                return False
        else:
            if total_big + small >= goal:
                return True
            else:
                return False
    else:
        return False

# # Optimal, divide and conquer.
# def make_bricks(small,big,goal):
#     # if there are less bricks in total
#     if small + big * 5 < goal:
#         return False
#     # if the surplus of the big bricks size exceeds the amount of small bricks available
#     if goal % 5 > small:
#         return False
#     return True
#
# print("0")
# print(make_bricks(3,1,12))
# print(make_bricks(7,1,12))
# print("1")
# print(make_bricks(1,2,12))
# print(make_bricks(2,2,12))
# print("2")
# print(make_bricks(1,3,15))
# print(make_bricks(3,3,15))
# print("3")
# print(make_bricks(1,3,12))
# print(make_bricks(3,3,12))
# print("4")
# print(make_bricks(3,2,8))
# print(make_bricks(3,2,9))
# print("5")
# print(make_bricks(1000000, 1000, 1000100))
# print(make_bricks(2, 1000000, 100003))

# how i resolved the issue
def lone_sum(a,b,c):
    if a == b or a == c:
        if a == b and a == c:
            return 0
        elif a == b:
            return c
        elif a == c:
            return b
    elif b == a or b == c:
        if b == a and b == c:
            return 0
        elif b == a:
            return c
        elif b == c:
            return a
    elif c == b or c == a:
        if c == b and c == a:
            return 0
        elif c == b:
            return a
        elif c == a:
            return b
    else:
        return a + b + c
#
# # the example solution
# def lone_sum(a, b, c):
#     sum = 0
#     if a != b and a != c: sum += a
#     if b != a and b != c: sum += b
#     if c != a and c != b: sum += c
#     return sum
#
# print(lone_sum(1,2,3))
# print(lone_sum(3,2,3))
# print(lone_sum(3,3,3))

def lucky_sum(a,b,c):
    if a == 13:
        return 0
    if b == 13:
        return a
    if c == 13:
        return a + b
    return a + b + c
# print(lucky_sum(1,2,3))
# print(lucky_sum(13,2,3))
# print(lucky_sum(1,13,3))
# print(lucky_sum(1,2,13))

# #region no_teen_sum
def fix_teen(n):
    if n >= 13 and n <= 19:
        if n in [15,16]:
            return n
        return 0
    return n

def no_teen_sum(a,b,c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)
# print(no_teen_sum(1,1,1))
# print(no_teen_sum(13,13,13))
# print(no_teen_sum(12,14,19))
# print(no_teen_sum(12,14,20))
# # print(fix_teen(12))
# # print(fix_teen(13))
# # print(fix_teen(15))
# # print(fix_teen(17))
# # print(fix_teen(20))
# #endregion no_teen_sum

def round10(num):
    if num % 10 >= 5:
        return num + (10 - num % 10)
    else:
        return num - num % 10

def round_sum(a,b,c):
    return round10(a) + round10(b) + round10(c)
# print(round_sum(16,17,18))
# print(round_sum(12,13,14))
# print(round_sum(6,4,4))
# print(round_sum(5,5,5))

def is_close(a,b):
    # print(abs(b - a))
    if abs(a - b) <= 1:
        return True
    return False

def is_far(a,b):
    # print(abs(a - b))
    if abs(a - b) >= 2:
        return True
    return False

def close_far(a,b,c):
    if is_close(a,b) and (is_far(c,a) and is_far(c,b)):
            return True
    elif is_close(a,c) and (is_far(b,a) and is_far(b,c)):
            return True
    return False
# print(close_far(1,2,10))
# print(close_far(1,2,3))
# print(close_far(4,1,3))
# print(is_close(1,2))
# print(is_close(1,3))
# print(is_close(1,4))
# print(is_close(4,1))
#
# print(is_far(1,2))
# print(is_far(1,3))
# print(is_far(1,4))
# print(is_far(4,1))

def make_chocolate(small,big,goal):
    # if there is less chocolate than the goal requires
    if small + big * 5 < goal:
        return -1
    # if there is too little of small to be used
    if goal % 5 > small:
        return -1

    # if the surplus of the big alone exceeds the amount of the goal, we must first find out how many we need before counting out the rest
    if big * 5 > goal:
        return int(goal - (int(goal / 5) * 5))
    # if the surplus of the big alone is less then the amout of the goal, we just need to calculate the need of the small ones
    elif big * 5 < goal:
        return int(goal - big * 5)
    # if there is not enough or too few or too many then there must be an even count to demand
    return 0
# print(make_chocolate(4,1,9))
# print(make_chocolate(4,1,10))
# print(make_chocolate(4,1,7))
# print(make_chocolate(6,2,7))
# print(make_chocolate(6,1,10))
