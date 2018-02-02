
def cigar_party(cigars, is_weekend):
    if is_weekend == True:
        if cigars >= 40:
            return True
        else:
            return False
    else:
        if cigars < 40:
            return False
        elif cigars >= 40 and cigars <= 60:
            return True
        else:
            return False
# print(cigar_party(30,False))
# print(cigar_party(50,False))
# print(cigar_party(70,True))

def date_fashion(you,date):
    if you >= 8 or date >= 8:
        if you <= 2 or date <= 2:
            return 0
        else:
            return 2
    else:
        if you <= 2 or date <= 2:
            return 0
        else:
            return 1
# print(date_fashion(5,10))
# print(date_fashion(5,2))
# print(date_fashion(5,5))

def squirrel_play(temp,is_summer):
    if is_summer == True:
        if temp < 60:
            return False
        elif temp >= 60 and temp <= 100:
            return True
        else:
            return False
    else:
        if temp < 60:
            return False
        elif temp >= 60 and temp <= 90:
            return True
        else:
            return False
# print(squirrel_play(70,False))
# print(squirrel_play(95,False))
# # print(squirrel_play(95,True))
#
# def caught_speeding(speed,is_birthday):
#     if is_birthday == True:
#         if speed <= 65:
#             return 0
#         elif speed >= 66 and speed <= 85:
#             return 1
#         else:
#             return 2
#     else:
#         if speed <= 60:
#             return 0
#         elif speed >= 61 and speed <= 80:
#             return 1
#         else:
#             return 2
#
def caught_speeding(speed,is_birthday):
    if is_birthday == True:
        speedLimitAddon = 5
    else:
        speedLimitAddon = 0
    if speed <= (60 + speedLimitAddon):
        return 0
    elif speed >= (61 + speedLimitAddon) and speed <= (80 + speedLimitAddon):
        return 1
    else:
        return 2
#
# print(caught_speeding(60,False))
# print(caught_speeding(65,False))
# print(caught_speeding(65,True))
# print(caught_speeding(95,True))

# def sorta_sum(a,b):
#     sum = a + b
#     if sum < 10:
#         return sum
#     elif sum >= 10 and sum <= 19:
#         return 20
#     else:
#         return sum

def sorta_sum(a,b):
    sum = a + b
    if sum >= 10 and sum <= 19:
        return 20
    return sum

# print(sorta_sum(3,4))
# print(sorta_sum(9,4))
# print(sorta_sum(10,11))

def alarm_clock(day,vacation):
    if day == 0 or day == 6:
        weekday = False
    else:
        weekday = True
    if vacation == True:
        if weekday == True:
            return "10:00"
        return "off"
    else:
        if weekday == True:
            return "7:00"
        return "10:00"
# print(alarm_clock(1,False))
# print(alarm_clock(1,True))
# print(alarm_clock(5,False))
# print(alarm_clock(5,True))
# print(alarm_clock(0,False))
# print(alarm_clock(0,True))

def love6(a,b):
    compareVal = 6
    if a == compareVal or b == compareVal:
        return True
    elif ( a + b ) == compareVal:
        return True
    elif ( a - b ) == compareVal or b - a == compareVal:
        return True
    else:
        return False
# print(love6(6,4))
# print(love6(4,5))
# print(love6(1,5))

def in1to10(n,outside_mode):
    if n >= 1 and n <= 10:
        if outside_mode:
            if n == 1 or n == 10:
                return True
            return False
        return True
    if outside_mode:
        return True
    return False
#
# print(in1to10(5, False))
# print(in1to10(11, False))
# print(in1to10(11, True))
# print(in1to10(9, True))

def near_ten(num):
    mod = num % 10
    if(mod <= 2) or ((10 - mod) <= 2):
        return True
    return False
# print(near_ten(12))
# print(near_ten(17))
# print(near_ten(19))
