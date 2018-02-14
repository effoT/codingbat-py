
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

# print(xyz_there('abcxyz'))
# print(xyz_there('abc.xyz'))
# print(xyz_there('xyz.abc'))
# print(xyz_there('abc.xyzxyz'))

'''
From here on the exercises are taken from java
'''

'''
bobThere
Return true if the given string contains a "bob" string, but where the middle 'o' char can be any char.
'''
# def bobThere(text):
#     import fnmatch
#     return fnmatch.fnmatchcase(text,'*b?b*')

def bobThere(text):
    if len(text) < 3:
        return False
    for i in range(len(text) - 2):
        if text[i] == "b" and text[i+2] == "b":
            return True
    return False

# print(bobThere("lskdjjb0bjkldf"))
# print(bobThere("lskdjjb00bjkldf"))
# print(bobThere("b9b"))
# print(bobThere("abcbob"))
# print(bobThere("bac"))
# print(bobThere("ba"))

'''
xyBalance 
We'll say that a String is xy-balanced if for all the 'x' chars in the string,
 there exists a 'y' char somewhere later in the string. So "xxy" is balanced, but "xyx" is not. 
 One 'y' can balance multiple 'x's. Return true if the given string is xy-balanced.
'''
def xyBalance(text):
    balance = True
    for i in range(len(text)):
        if text[i] == "x":
            balance = False
        elif text[i] == "y":
            balance = True
    return balance


# if xyBalance("aaxbby") != True: print('xyBalance("aaxbby") not True')
# if xyBalance("aaxbb") != False: print('xyBalance("aaxbb") not False')
# if xyBalance("bbb") != True: print('xyBalance("bbb") not True')
# if xyBalance("") != True: print('xyBalance("") not True')
# if xyBalance("yxyxyxyx") != False: print('xyBalance("yxyxyxyx") not False')
# if xyBalance("yxyxyxyxy") != True: print('xyBalance("yxyxyxyxy") not True')
# if xyBalance("12xabxxydxyxyzz") != True: print('xyBalance("12xabxxydxyxyzz") not True')

'''
mixString 
Given two strings, a and b, create a bigger string made of the first char of a, the first char of b, 
the second char of a, the second char of b, and so on. Any leftover chars go at the end of the result.
'''

def mixString(a,b):
    newString = ""
    for i in range(max(len(a),len(b))):
        if (len(a) - 1) >= i:
            newString += a[i]
        if (len(b) - 1) >= i:
            newString += b[i]
    return newString
# print(mixString("Hi", "There"))
# print(mixString("xxxx", "There"))

'''
repeatEnd 
Given a string and an int n, return a string made of n repetitions of the last n characters of the string. 
You may assume that n is between 0 and the length of the string, inclusive.
'''

def repeatEnd(a,b):
    result = ""
    for i in range(0,b):
        result += a[-b:]
    return result


# print(repeatEnd("Hello", 3))
# print(repeatEnd("Hello", 2))
# print(repeatEnd("Hello", 1))

'''
repeatFront
Given a string and an int n, return a string made of the first n characters of the string, 
followed by the first n-1 characters of the string, and so on. You may assume that n is between 0 and the length of the string, 
inclusive (i.e. n >= 0 and n <= str.length()).
'''

def repeatFront(text,num):
    result = ""
    for i in range(num,0,-1):
        result += text[0:i]
    return result

# print(repeatFront("Chocolate", 4))
# print(repeatFront("Chocolate", 3))
# print(repeatFront("Ice Cream", 2))
# print(repeatFront("Ice Cream", 5))

'''
repeatSeparator
Given two strings, word and a separator sep, return a big string made of count occurrences of the word, 
separated by the separator string.
'''

def repeatSeparator(word,sep,count):
    string = ""
    for o in range(count):
        if o < count:
            string += word
        if o < count -1:
            string += sep
    return string


# if repeatSeparator("Word", "X", 3) != "WordXWordXWord": print('repeatSeparator("Word", "X", 3) not "WordXWordXWord"')
# if repeatSeparator("This", "And", 2) != "ThisAndThis": print('repeatSeparator("This", "And", 2) not "ThisAndThis"')
# if repeatSeparator("This", "And", 1) != "This": print('repeatSeparator("This", "And", 1) not "This"')
# if repeatSeparator("Hi", "-n-", 2) != "Hi-n-Hi": print('repeatSeparator("Hi", "-n-", 2) not "Hi-n-Hi"')
# if repeatSeparator("AAA", "", 1) != "AAA": print('repeatSeparator("AAA", "", 1) not "AAA"')
# if repeatSeparator("AAA", "", 0) != "": print('repeatSeparator("AAA", "", 0) not ""')
# if repeatSeparator("A", "B", 5) != "ABABABABA": print('repeatSeparator("A", "B", 5) not "ABABABABA"')
# if repeatSeparator("abc", "XX", 3) != "abcXXabcXXabc": print('repeatSeparator("abc", "XX", 3) not "abcXXabcXXabc"')
# if repeatSeparator("abc", "XX", 2) != "abcXXabc": print('repeatSeparator("abc", "XX", 2)  print "abcXXabc"')
# if repeatSeparator("abc", "XX", 1) != "abc": print('repeatSeparator("abc", "XX", 1) not"abc" ')
# if repeatSeparator("XYZ", "a", 2) != "XYZaXYZ": print('repeatSeparator("XYZ", "a", 2) not "XYZaXYZ"')

'''
prefixAgain
Given a string, consider the prefix string made of the first N chars of the string. 
Does that prefix string appear somewhere else in the string? Assume that the string is not empty and that N 
is in the range 1..str.length().
'''
#attempt one
# def prefixAgain(string,n):
#     if len(string) == 2:
#         if string[0] == string[1]:
#             return True
#         return False

#     for o in range(n,len(string)-n):
#         if string[0:n] == string[o:o+n]:
#             return True
#     return False


def prefixAgain(string, n):
    for o in range(n-1, len(string)-n):
        if string[0:n] == string[n+o:n+o+n]:
            return True
    return False
        

# if prefixAgain("abXYabc", 1) != True: print('prefixAgain("abXYabc", 1) not True')
# if prefixAgain("abXYabc", 2) != True: print('prefixAgain("abXYabc", 2) not True')
# if prefixAgain("abXYabc", 3) != False: print('prefixAgain("abXYabc", 3) not False')
# if prefixAgain("xyzxyxyxy", 2) != True: print('prefixAgain("xyzxyxyxy", 2) not True')
# if prefixAgain("xyzxyxyxy", 3) != False: print('prefixAgain("xyzxyxyxy", 3) not False')
# if prefixAgain("Hi12345Hi6789Hi10", 1) != True: print('prefixAgain("Hi12345Hi6789Hi10", 1) not True')
# if prefixAgain("Hi12345Hi6789Hi10", 2) != True: print('prefixAgain("Hi12345Hi6789Hi10", 2) not True')
# if prefixAgain("Hi12345Hi6789Hi10", 3) != True: print('prefixAgain("Hi12345Hi6789Hi10", 3) not True')
# if prefixAgain("Hi12345Hi6789Hi10", 4) != False: print('prefixAgain("Hi12345Hi6789Hi10", 4) not False')
# if prefixAgain("a", 1) != False: print('prefixAgain("a", 1) not False')
# if prefixAgain("aa", 1) != True: print('prefixAgain("aa", 1) not True')
# if prefixAgain("ab", 1) != False: print('prefixAgain("ab", 1) not False')

'''
xyzMiddle
Given a string, does "xyz" appear in the middle of the string? To define middle,
 we'll say that the number of chars to the left and right of the "xyz" must differ by at most one. 
 This problem is harder than it looks.
'''

def xyzMiddle(strIn):
    if len(strIn) < 3:
        return False
    for i in range(len(strIn)-1):
        if strIn[i-1] == "x" and strIn[i] == "y" and strIn[i+1] == "z":
            if abs(len(strIn[:i]) - len(strIn[(i+1):])) < 2:
                return True
    return False


# if xyzMiddle("AAxyzBB") != True: print('xyzMiddle("AAxyzBB") not True')
# if xyzMiddle("AxyzBB") != True: print('xyzMiddle("AxyzBB") not True')
# if xyzMiddle("AxyzBBB") != False: print('xyzMiddle("AxyzBBB") not False')
# if xyzMiddle("AxyzBBBB") != False: print('xyzMiddle("AxyzBBBB") not False')
# if xyzMiddle("AAAxyzB") != False: print('xyzMiddle("AAAxyzB") not False')
# if xyzMiddle("AAAxyzBB") != True: print('xyzMiddle("AAAxyzBB") not True')
# if xyzMiddle("AAAAxyzBB") != False: print('xyzMiddle("AAAAxyzBB") not False')
# if xyzMiddle("AAAAAxyzBBB") != False: print('xyzMiddle("AAAAAxyzBBB") not False')
# if xyzMiddle("1x345xyz12x4") != True: print('xyzMiddle("1x345xyz12x4") not True')
# if xyzMiddle("xyzAxyzBBB") != True: print('xyzMiddle("xyzAxyzBBB") not True')
# if xyzMiddle("xyzAxyzBxyz") != True: print('xyzMiddle("xyzAxyzBxyz") not True')
# if xyzMiddle("xyzxyzAxyzBxyzxyz") != True: print('xyzMiddle("xyzxyzAxyzBxyzxyz") not True')
# if xyzMiddle("xyzxyzxyzBxyzxyz") != True: print('xyzMiddle("xyzxyzxyzBxyzxyz") not True')
# if xyzMiddle("xyzxyzAxyzxyzxyz") != True: print('xyzMiddle("xyzxyzAxyzxyzxyz") not True')
# if xyzMiddle("xyzxyzAxyzxyzxy") != False: print('xyzMiddle("xyzxyzAxyzxyzxy") not False')
# if xyzMiddle("AxyzxyzBB") != False: print('xyzMiddle("AxyzxyzBB") not False')
# if xyzMiddle("") != False: print('xyzMiddle("") not False')
# if xyzMiddle("x") != False: print('xyzMiddle("x") not False')
# if xyzMiddle("xy") != False: print('xyzMiddle("xy") not False')
# if xyzMiddle("xyz") != True: print('xyzMiddle("xyz") not True')
# if xyzMiddle("xyzz") != True: print('xyzMiddle("xyzz") not True')
