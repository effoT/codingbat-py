
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
