
def double_char(string):
    new_string = ""
    for i in range(len(string)):
        # print(string[i])
        new_string += (string[i] + string[i])
    return new_string
# print(double_char("The"))
# print(double_char("AAbb"))
# print(double_char("Hi-There"))

# # How I solved it
def count_hi(string):
    counter = 0
    for i in range(len(string) - 1 ):
        if string[i] + string[(i + 1)] == 'hi':
            counter += 1
    return counter
#
# # Alternative solution
# def count_hi(str):
#   sum = 0
#   ## Loop to length-1 and access index i and i+1
#   ## in the loop.
#   for i in range(len(str)-1):
#     if str[i:i+2] == 'hi':
#       sum = sum + 1
#   return sum
#
# print(count_hi('abc hi ho'))
# print(count_hi('ABC hi hi'))
# print(count_hi('hihi'))

def cat_dog(string):
    catCounter = 0
    dogCounter = 0
    for i in range(len(string) - 2):
        if string[i:i+3] == 'cat':
            catCounter += 1
        elif string[i:i+3] == 'dog':
            dogCounter += 1
    if catCounter == dogCounter:
        return True
    return False
# print(cat_dog('catdog'))
# print(cat_dog('catcat'))
# print(cat_dog('1cat1cadodog'))

def count_code(string):
    counter = 0
    for i in range(len(string) - 3):
        if string[i:(i + 2)] == 'co' and string[(i + 3):(i + 4)] == 'e':
            counter += 1
    return counter
# print(count_code("aaacodebbb"))
# print(count_code("codexxcode"))
# print(count_code("cozexxcope"))

# # This solution was written for the wrong purpose, it checks if the longer of the strings begins or ends with the shorter one
# def end_other(a,b):
#     string1 = a.lower()
#     string2 = b.lower()
#     if len(string2) > len(string1):
#         if string2[0:(len(string1))] == string1 or string2[(len(string1)*-1)::] == string1:
#             return True
#     if string1[0:(len(string2))] == string2 or string1[(len(string2)*-1)::] == string2:
#         return True
#     return False

def end_other(a, b):
  a = a.lower()
  b = b.lower()
  #return (b.endswith(a) or a.endswith(b))
  return a[-(len(b)):] == b or a == b[-(len(a)):] 
# print(end_other('Hiabc', 'abc'))
# print(end_other('AbC', 'HiaBc'))
# print(end_other('abc', 'abXabc'))
# print(end_other('Hiabc', 'bca'))
# print(end_other('ab', 'ab12'))

def xyz_there(string):
    for i in range(len(string)):
        if string[i : (i + 3)] == "xyz" and string[(i -1)] != chr(46):
            return True
    return False

print(xyz_there('abcxyz'))
print(xyz_there('abc.xyz'))
print(xyz_there('xyz.abc'))
print(xyz_there('abc.xyzxyz'))

