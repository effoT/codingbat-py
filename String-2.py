
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


'''
getSandwich
A sandwich is two pieces of bread with something in between. Return the string that is between the first and last 
appearance of "bread" in the given string, or return the empty string "" if there are not two pieces of bread.
'''

def getSandwich(inStr):
    bread_first_finish = 0
    bread_last_start = 0
    if len(inStr) < 5:
        return ""
    
    for o in range(len(inStr) -4):
        # print(inStr[o:o+5])
        if inStr[o:o+5] == "bread" and bread_first_finish == 0:
            bread_first_finish = o + 5
            # print(o + 5)
        elif inStr[o:o+5] == "bread" and bread_first_finish != 0:
            bread_last_start = o
            # print(o)
    if bread_first_finish != 0 and bread_last_start != 0:
        return inStr[bread_first_finish:bread_last_start]
    else:
        return ""


# if getSandwich("breadjambread") != "jam": print('getSandwich("breadjambread") not jam')
# if getSandwich("xxbreadjambreadyy") != "jam": print('getSandwich("xxbreadjambreadyy") not jam')
# if getSandwich("xxbreadyy") != "": print('getSandwich("xxbreadyy") not ""')
# if getSandwich("xxbreadbreadjambreadyy") != "breadjam": print('getSandwich("xxbreadbreadjambreadyy") not "breadjam"')
# if getSandwich("breadAbread") != "A": print('getSandwich("breadAbread") not !')
# if getSandwich("breadbread") != "": print('getSandwich("breadbread") not ""')
# if getSandwich("abcbreaz") != "": print('getSandwich("abcbreaz") not ""')
# if getSandwich("xyz") != "": print('getSandwich("xyz") not ""')
# if getSandwich("") != "": print('getSandwich("") not ""')
# if getSandwich("breadbreaxbread") != "breax": print('getSandwich("breadbreaxbread") not "breax"')
# if getSandwich("breaxbreadybread") != "y": print('getSandwich("breaxbreadybread") not "y"')
# if getSandwich("breadbreadbreadbread") != "breadbread": print('getSandwich("breadbreadbreadbread") not "breadbread"')

'''
sameStarChar
Returns true if for every '*' (star) in the string, if there are chars both immediately before and after the star, 
they are the same.
'''
def sameStarChar(inStr):
    out_status = True
    for o in range(len(inStr)):
        if o > 0 and o < (len(inStr) -1) and inStr[o] == chr(42):
            if inStr[o - 1] == inStr[o + 1]:
                out_status = True
            else:
                out_status = False
    return out_status


# if sameStarChar("xy*yzz") != True: print('sameStarChar("xy*yzz") not True')
# if sameStarChar("xy*zzz") != False: print('sameStarChar("xy*zzz") not Falsa')
# if sameStarChar("*xa*az") != True: print('sameStarChar("*xa*az") not True')
# if sameStarChar("*xa*bz") != False: print('sameStarChar("*xa*bz") not False')
# if sameStarChar("*xa*a*") != True: print('sameStarChar("*xa*a*") not True')
# if sameStarChar("") != True: print('sameStarChar("") not True')
# if sameStarChar("*xa*a*a") != True: print('sameStarChar("*xa*a*a") not True')
# if sameStarChar("*xa*a*b") != False: print('sameStarChar("*xa*a*b") not False')
# if sameStarChar("*12*2*2") != True: print('sameStarChar("*12*2*2") not True')
# if sameStarChar("12*2*3*") != False: print('sameStarChar("12*2*3*") not False')
# if sameStarChar("abcDEF") != True: print('sameStarChar("abcDEF") not True')
# if sameStarChar("XY*YYYY*Z*") != False: print('sameStarChar("XY*YYYY*Z*") not False')
# if sameStarChar("XY*YYYY*Y*") != True: print('sameStarChar("XY*YYYY*Y*") not True')
# if sameStarChar("12*2*3*") != False: print('sameStarChar("12*2*3*") not False')
# if sameStarChar("*") != True: print('sameStarChar("*") not True')
# if sameStarChar("**") != True: print('sameStarChar("**") not True')

'''
oneTwo
Given a string, compute a new string by moving the first char to come after the next two chars, 
so "abc" yields "bca". Repeat this process for each subsequent group of 3 chars, so "abcdef" yields "bcaefd". 
Ignore any group of fewer than 3 chars at the end.
'''
def oneTwo(inStr):
    new_word = "1"
    counter = 0
    if len(inStr) < 3:
        return ""
    for o in range(len(inStr) // 3):
        new_word += inStr[(counter + 1)]
        new_word += inStr[(counter + 2)]
        new_word += inStr[(counter)]
        counter += 3
    return new_word


# if oneTwo("abc") != "bca": print('oneTwo("abc") not "bca"')
# if oneTwo("tca") != "cat": print('oneTwo("tca") not "cat"')
# if oneTwo("tcagdo") != "catdog": print('oneTwo("tcagdo") not "catdog"')
# if oneTwo("chocolate") != "hocolctea": print('oneTwo("chocolate") not "hocolctea"')
# if oneTwo("1234567890") != "231564897": print('oneTwo("1234567890") not "231564897"')
# if oneTwo("xabxabxabxabxabxabxab") != "abxabxabxabxabxabxabx": print('oneTwo("xabxabxabxabxabxabxab") not "abxabxabxabxabxabxabx"')
# if oneTwo("abcdefx") != "bcaefd": print('oneTwo("abcdefx") not "bcaefd"')
# if oneTwo("abcdefxy") != "bcaefd": print('oneTwo("abcdefxy") not "bcaefd"')
# if oneTwo("abcdefxyz") != "bcaefdyzx": print('oneTwo("abcdefxyz") not "bcaefdyzx"')
# if oneTwo("") != "": print('oneTwo("") not ""') 
# if oneTwo("x") != "": print('oneTwo("x") not ""')
# if oneTwo("xyz") != "yzx": print('oneTwo("xyz") not "yzx"')
# if oneTwo("abcdefghijklkmnopqrstuvwxyz1234567890") != "bcaefdhigkljmnkpqostrvwuyzx231564897": print('oneTwo("abcdefghijklkmnopqrstuvwxyz1234567890") not "bcaefdhigkljmnkpqostrvwuyzx231564897"')
# if oneTwo("abcdefghijklkmnopqrstuvwxyz123456789") != "bcaefdhigkljmnkpqostrvwuyzx231564897": print('oneTwo("abcdefghijklkmnopqrstuvwxyz123456789") not "bcaefdhigkljmnkpqostrvwuyzx231564897"')
# if oneTwo("abcdefghijklkmnopqrstuvwxyz12345678") != "bcaefdhigkljmnkpqostrvwuyzx231564": print('oneTwo("abcdefghijklkmnopqrstuvwxyz12345678") not "bcaefdhigkljmnkpqostrvwuyzx231564"')

'''
zipZap 
Look for patterns like "zip" and "zap" in the string -- length-3, starting with 'z' and ending with 'p'.
Return a string where for all such words, the middle letter is gone, so "zipXzap" yields "zpXzp".
'''
# crate a list of what to omit and print out every location that is not in the list
# def zipZap(text):
#     no_return_list = []
#     new_text = ""
#     for o in range(1,len(text) - 1):
#         if text[o-1] == "z" and text[o+1] == "p":
#             no_return_list += [o]
    
#     for o in range(len(text)):
#         if o not in no_return_list:
#             new_text += text[o]
#     return new_text

# do it with one loop by altering the original text and counting by its updated length and chars
def zipZap(text):
    o = 0
    while(o < len(text) -2):
        if text[o] == "z" and text[o+2] == "p":
            temp_text = text[:(o+1)]
            temp_text += text[(o+2):]
            text = temp_text
        o += 1
    return text


# if zipZap("zipXzap") != "zpXzp": print('zipZap("zipXzap") not "zpXzp"')
# if zipZap("zopzop") != "zpzp": print('zipZap("zopzop") not "zpzp"')
# if zipZap("zzzopzop") != "zzzpzp": print('zipZap("zzzopzop") not "zzzpzp"')
# if zipZap("zibzap") != "zibzp": print('zipZap("zibzap") not "zibzp"')
# if zipZap("zip") != "zp": print('zipZap("zip") not "zp"')
# if zipZap("zi") != "zi": print('zipZap("zi") not "zi"')
# if zipZap("z") != "z": print('zipZap("z") not "z"')
# if zipZap("") != "": print('zipZap("") not ""')
# if zipZap("zzp") != "zp": print('zipZap("zzp") not "zp"')
# if zipZap("abcppp") != "abcppp": print('zipZap("abcppp") not "abcppp"')
# if zipZap("azbcppp") != "azbcppp": print('zipZap("azbcppp") not "azbcppp"')
# if zipZap("azbcpzpp") != "azbcpzp": print('zipZap("azbcpzpp") not "azbcpzp"')

'''
starOut
Return a version of the given string, where for every star (*) in the string the star and the chars 
immediately to its left and right are gone. So "ab*cd" yields "ad" and "ab**cd" also yields "ad".
'''
def starOut(text):
    new_text = ""
    for o in range(len(text)):
        if o == 0 and len(text) > 1:
            if text[o] != chr(42) and text[o+1] != chr(42):
                new_text += text[o]
        elif (len(text) - 1) > o:  
            if text[o-1] != chr(42) and text[o] != chr(42) and text[o+1] != chr(42):
                new_text += text[o]
        elif (len(text) - 1) == o:
             if text[o-1] != chr(42) and text[o] != chr(42):
                new_text += text[o]
    return new_text


# if starOut("ab*cd") != "ad": print('starOut("ab*cd")  not "ad"')
# if starOut("ab**cd") != "ad": print('starOut("ab**cd")  not "ad"')
# if starOut("sm*eilly") != "silly": print('starOut("sm*eilly")  not "silly"')
# if starOut("sm*eil*ly") != "siy": print('starOut("sm*eil*ly")  not "siy"')
# if starOut("sm**eil*ly") != "siy": print('starOut("sm**eil*ly")  not "siy"')
# if starOut("sm***eil*ly") != "siy": print('starOut("sm***eil*ly")  not "siy"')
# if starOut("stringy*") != "string": print('starOut("stringy*")  not "string"')
# if starOut("*stringy") != "tringy": print('starOut("*stringy")  not "tringy"')
# if starOut("*str*in*gy") != "ty": print('starOut("*str*in*gy")  not "ty"')
# if starOut("abc") != "abc": print('starOut("abc")  not "abc"')
# if starOut("a*bc") != "c": print('starOut("a*bc")  not "c"')
# if starOut("ab") != "ab": print('starOut("ab")  not "ab"')
# if starOut("a*b") != "": print('starOut("a*b")  not ""')
# if starOut("a") != "a": print('starOut("a")  not "a"')
# if starOut("a*") != "": print('starOut("a*")  not ""')
# if starOut("*a") != "": print('starOut("*a")  not ""')
# if starOut("*") != "": print('starOut("*")  not ""')
# if starOut("") != "": print('starOut("")  not ""')


'''
plusOut
Given a string and a non-empty word string, return a version of the original String where all chars 
have been replaced by pluses ("+"), except for appearances of the word string which are preserved unchanged.
'''
# using 2 loops
# def plusOut(text,word):
#     locations = []
#     new_word = ""
#     # first gather the locations of the given word letters
#     for o in range(len(text) - len(word) + 1):
#         if text[o:o+len(word)] == word:
#             for i in range(len(word)):
#                 locations += [(i + o)]
    
#     #loop through the locations of the given word letters and write them into new string as desired
#     for o in range(len(text)):
#         if o in locations:
#             new_word += text[o]
#         else:
#             new_word += "+"
#     return new_word

# using 1 loop
def plusOut(text, word):
    new_text = ""
    o = 0
    while(o < len(text)):
        if text[o:o+len(word)] == word:
            new_text += word
            o += len(word)
        else:
            new_text += "+"
            o += 1
    return new_text


# if plusOut("12xy34", "xy")  != "++xy++": print('plusOut("12xy34", "xy")  not "++xy++"')
# if plusOut("12xy34", "1") != "1+++++": print('plusOut("12xy34", "1")  not "1+++++"')
# if plusOut("12xy34xyabcxy", "xy") != "++xy++xy+++xy": print('plusOut("12xy34xyabcxy", "xy")  not "++xy++xy+++xy"')
# if plusOut("abXYabcXYZ", "ab") != "ab++ab++++": print('plusOut("abXYabcXYZ", "ab")  not "ab++ab++++"')
# if plusOut("abXYabcXYZ", "abc") != "++++abc+++": print('plusOut("abXYabcXYZ", "abc")  not "++++abc+++"')
# if plusOut("abXYabcXYZ", "XY") != "++XY+++XY+": print('plusOut("abXYabcXYZ", "XY")  not "++XY+++XY+"')
# if plusOut("abXYxyzXYZ", "XYZ") != "+++++++XYZ": print('plusOut("abXYxyzXYZ", "XYZ")  not "+++++++XYZ"')
# if plusOut("--++ab", "++") != "++++++": print('plusOut("--++ab", "++")  not "++++++"')
# if plusOut("aaxxxxbb", "xx") != "++xxxx++": print('plusOut("aaxxxxbb", "xx")  not "++xxxx++"')
# if plusOut("123123", "3") != "++3++3": print('plusOut("123123", "3")  not "++3++3"')

'''
wordEnds
Given a string and a non-empty word string, return a string made of each char just before and just after 
every appearance of the word in the string. Ignore cases where there is no cha before or after the word, 
and a char may be included twice if it is between two words.
'''
def wordEnds(text,word):
    if len(text) <= len(word):
        return ""
    new_word = ""
    for o in range(len(text) - len(word) + 1):
        # check if first instance
        if o == 0:
            if text[o:o+len(word)] == word:
                new_word += text[o+len(word)]
            # check if last instance
        elif o == len(text) - len(word):
            if text[o:o+len(word)] == word:
                new_word += text[o - 1]
            # must be in the middle
        else:
            if text[o:o+len(word)] == word:
                new_word += text[o - 1]
                new_word += text[o + len(word)]
    return new_word


# if wordEnds("abcXY123XYijk", "XY") != "c13i": print('wordEnds("abcXY123XYijk", "XY")  not "c13i"')
# if wordEnds("XY123XY", "XY") != "13": print('wordEnds("XY123XY", "XY")  not "13"')
# if wordEnds("XY1XY", "XY") != "11": print('wordEnds("XY1XY", "XY")  not "11"')
# if wordEnds("XYXY", "XY") != "XY": print('wordEnds("XYXY", "XY")  not "XY"')
# if wordEnds("XY", "XY") != "": print('wordEnds("XY", "XY")  not ""')
# if wordEnds("Hi", "XY") != "": print('wordEnds("Hi", "XY")  not ""')
# if wordEnds("", "XY") != "": print('wordEnds("", "XY")  not ""')
# if wordEnds("abc1xyz1i1j", "1") != "cxziij": print('wordEnds("abc1xyz1i1j", "1")  not "cxziij"')
# if wordEnds("abc1xyz1", "1") != "cxz": print('wordEnds("abc1xyz1", "1")  not "cxz"')
# if wordEnds("abc1xyz11", "1") != "cxz11": print('wordEnds("abc1xyz11", "1")  not "cxz11"')
# if wordEnds("abc1xyz1abc", "abc") != "11": print('wordEnds("abc1xyz1abc", "abc")  not "11"')
# if wordEnds("abc1xyz1abc", "b") != "acac": print('wordEnds("abc1xyz1abc", "b")  not "acac"')
# if wordEnds("abc1abc1abc", "abc") != "1111": print('wordEnds("abc1abc1abc", "abc")  not "1111"')
