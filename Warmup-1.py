def sleep_in(weekday, vacation):
  if weekday == True and vacation == True:
      return True
  elif weekday == True and vacation == False:
      return False
  elif weekday == False and vacation == True:
      return True
  else:
    return True
# print(sleep_in(False,False))
# print(sleep_in(True,False))
# print(sleep_in(False,True))

def monkey_trouble(a_smile, b_smile):
    if ((a_smile == True and b_smile == True) or (a_smile == False and b_smile == False)):
        return True
    else:
        return False
# print(monkey_trouble(True,False))
# print(monkey_trouble(False,True))
# print(monkey_trouble(True,True))
# print(monkey_trouble(False,False))

def sum_double(a,b):
    if a == b:
        return (a + b) * 2
    else:
        return a + b
# print(sum_double(1,2))
# print(sum_double(2,2))
# print(sum_double(3,2))

def diff21(n):
    if n > 21:
        return (n - 21) * 2
    else:
        return 21 - n
# print(diff21(34))
# print(diff21(11))
# print(diff21(0))
# print(diff21(-5))

def parrot_trouble(talking,hour):
    if talking == True and (hour < 7 or hour > 20):
        return True
    else:
        return False

# print(parrot_trouble(True,6))
# print(parrot_trouble(True,7))
# print(parrot_trouble(False,6))

def makes10(a,b):
    if a == 10 or b == 10:
        return True
    elif a + b == 10:
        return True
    else:
        return False
# print(makes10(9,10))
# print(makes10(9,9))
# print(makes10(1,9))

def near_hundred(n):
    if (100 - n <= 10 and 100 - n >= -10) or (200 - n <= 10 and 200 - n >= -10):
        return True
    else:
        return False
# print(near_hundred(93))
# print(near_hundred(90))
# print(near_hundred(89))
# print(near_hundred(111))
# print(near_hundred(209))
# print(near_hundred(110))
# print(near_hundred(210))

def pos_neg(a,b,negative):
    if (a < 0 and b < 0) and (negative != True):
        return False
    elif (a < 0 and b < 0) and (negative == True):
        return True
    elif (a < 0 or b < 0 ) and (negative != True):
        return True
    else:
        return False
# print(pos_neg(1,-1,False))
# print(pos_neg(-1,1,False))
# print(pos_neg(-4,-5,True))
# print(pos_neg(1,-1,True))
# print(pos_neg(1,1,False))
# print(pos_neg(-1, -1, False))

def not_string(str):
    if str.startswith('not'):
        return(str)
    else:
        return("not {}".format(str))
# print(not_string("candy"))
# print(not_string("x"))
# print(not_string("not bad"))
# print(not_string("is not"))

def missing_char(str,n):
    str = str[:n] + str[(n+1):]
    return str
# print(missing_char("missing",4))

def front_back(str):
    if len(str) == 1:
        return str
    else:
        return str[-1:] + str[1:-1] + str[:1]
# print(front_back('Chocolate'))
# print(front_back('c'))

def front3(str):
    return str[:3] + str[:3] + str[:3]
# print(front3("jotain"))
