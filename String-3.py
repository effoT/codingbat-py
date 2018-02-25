# these are problems at codingbat.com for java, testing them out on python

'''
countYZ
Given a string, count the number of words ending in 'y' or 'z' -- so the 'y' in "heavy" and the 'z' in 
"fez" count, but not the 'y' in "yellow" (not case sensitive). We'll say that a y or z is at the end of 
a word if there is not an alphabetic letter immediately following it. (Note: Character.isLetter(char) 
tests if a char is an alphabetic letter.)
'''
# space = 32
def countYZ(text):
    counter = 0
    # set the entire string to lowercase to remove the case sensitivity
    text = text.lower()
    for o in range(len(text)):
        # if last character, so that we don't try to run out of index and so that we can test the last character
        if o == len(text) -1: 
            if text[o] == "y" or text[o] == "z":
                counter += 1
        else:
            # remember to check that the next character is not an alpha
            if (text[o] == "y" or text[o] == "z") and text[(o+1)].isalpha() == False:
                counter += 1
    return counter


# if countYZ("fez day") != 2: print('countYZ("fez day")  not 2')
# if countYZ("day fez") != 2: print('countYZ("day fez")  not 2')
# if countYZ("day fyyyz") != 2: print('countYZ("day fyyyz")  not 2')
# if countYZ("day yak") != 1: print('countYZ("day yak")  not 1')
# if countYZ("day:yak") != 1: print('countYZ("day:yak")  not 1')
# if countYZ("!!day--yaz!!") != 2: print('countYZ("!!day--yaz!!")  not 2')
# if countYZ("yak zak") != 0: print('countYZ("yak zak")  not 0')
# if countYZ("DAY abc XYZ") != 2:print('countYZ("DAY abc XYZ")  not 2')
# if countYZ("aaz yyz my") != 3: print('countYZ("aaz yyz my")  not 3')
# if countYZ("y2bz") != 2: print('countYZ("y2bz")  not 2')
# if countYZ("zxyx") != 0: print('countYZ("zxyx")  not 0')

'''
withoutString
Given two strings, base and remove, return a version of the base string where all instances of 
the remove string have been removed (not case sensitive). You may assume that the remove string 
is length 1 or more. Remove only non-overlapping instances, so with "xxx" removing "xx" leaves "x".
'''

def withoutString(text, remove):
    import re
    while(True):
        # try if there is an index remaining
        try:
            pos = (text.lower()).index(remove.lower())
        except:
            break

        temp_text = text[0:pos]
        temp_text += text[(pos + len(remove)):]
        text = temp_text
    return re.sub(' +', ' ', text)

# if withoutString("Hello there", "llo") != "He there": print('withoutString("Hello there", "llo")  not "He there"')
# if withoutString("Hello there", "e") != "Hllo thr": print('withoutString("Hello there", "e")  not "Hllo thr"')
# if withoutString("Hello there", "x") != "Hello there": print('withoutString("Hello there", "x")  not "Hello there"')
# if withoutString("This is a FISH", "IS") != "Th a FH": print('withoutString("This is a FISH", "IS")  not "Th a FH"')
# if withoutString("THIS is a FISH", "is") != "TH a FH": print('withoutString("THIS is a FISH", "is")  not "TH a FH"')
# if withoutString("THIS is a FISH", "iS") != "TH a FH": print('withoutString("THIS is a FISH", "iS")  not "TH a FH"')
# if withoutString("abxxxxab", "xx") != "abab": print('withoutString("abxxxxab", "xx")  not "abab"')
# if withoutString("abxxxab", "xx") != "abxab": print('withoutString("abxxxab", "xx")  not "abxab"')
# if withoutString("abxxxab", "x") != "abab": print('withoutString("abxxxab", "x")  not "abab"')
# if withoutString("xxx", "x") != "": print('withoutString("xxx", "x")  not ""')
# if withoutString("xxx", "xx") != "x": print('withoutString("xxx", "xx")  not "x"')
# if withoutString("xyzzy", "Y") != "xzz": print('withoutString("xyzzy", "Y")  not "xzz"')
# if withoutString("", "x") != "": print('withoutString("", "x")  not ""')
# if withoutString("abcabc", "b") != "acac": print('withoutString("abcabc", "b")  not "acac"')
# if withoutString("AA22bb", "2") != "AAbb": print('withoutString("AA22bb", "2")  not "AAbb"')
# if withoutString("1111", "1") != "": print('withoutString("1111", "1")  not ""')
# if withoutString("1111", "11") != "": print('withoutString("1111", "11")  not ""')
# if withoutString("MkjtMkx", "Mk") != "jtx": print('withoutString("MkjtMkx", "Mk")  not "jtx"')
# if withoutString("Hi HoHo", "Ho") != "Hi ": print('withoutString("Hi HoHo", "Ho")  not "Hi "')

'''
equalIsNot
Given a string, return true if the number of appearances of "is" anywhere in the string is 
equal to the number of appearances of "not" anywhere in the string (case sensitive).
'''

def equalIsNot(text):
    not_count = 0
    is_count = 0
    for o in range(len(text)):
        if o <= len(text) -1: #is
            if text[o:o+2] == "is":
                is_count += 1
        if o <= len(text) -2: #not
            if text[o:o + 3] == "not":
                not_count += 1
    return not_count == is_count


# if equalIsNot("This is not") != False: print('equalIsNot("This is not")  not False')
# if equalIsNot("This is notnot") != True: print('equalIsNot("This is notnot")  not True')
# if equalIsNot("noisxxnotyynotxisi") != True: print('equalIsNot("noisxxnotyynotxisi")  not True')
# if equalIsNot("noisxxnotyynotxsi") != False: print('equalIsNot("noisxxnotyynotxsi")  not False')
# if equalIsNot("xxxyyyzzzintint") != True: print('equalIsNot("xxxyyyzzzintint")  not True')
# if equalIsNot("") != True: print('equalIsNot("")  not True')
# if equalIsNot("isisnotnot") != True: print('equalIsNot("isisnotnot")  not True')
# if equalIsNot("isisnotno7Not") != False: print('equalIsNot("isisnotno7Not")  not False')
# if equalIsNot("isnotis") != False: print('equalIsNot("isnotis")  not False')
# if equalIsNot("mis3notpotbotis") != False: print('equalIsNot("mis3notpotbotis")  not False')

'''
gHappy
We'll say that a lowercase 'g' in a string is "happy" if there is another 'g' immediately to its left or right. 
Return true if all the g's in the given string are happy.
'''

def gHappy(text):
    # gotta be a happy g if it does not exist
    if "g" not in text:
        return True
    # if there is only one char and it's g, the g cannot be happy
    if len(text) == 1:
        return False

    # test the mid area
    for o in range(1,len(text) -1):
        if text[o-1] != "g" and text[o+1] != "g" and text[o] == "g":
            return False
    
    # at last check the last element, so that we won't end up in index out of range problem
    if len(text) > 1 and text[-1] == "g" and text[-2] != "g":
        return False
    return True


# if gHappy("xxggxx") != True: print('gHappy("xxggxx")  not True')
# if gHappy("xxgxx") != False: print('gHappy("xxgxx")  not False')
# if gHappy("xxggyygxx") != False: print('gHappy("xxggyygxx")  not False')
# if gHappy("g") != False: print('gHappy("g")  not False')
# if gHappy("gg") != True: print('gHappy("gg")  not True')
# if gHappy("") != True: print('gHappy("")  not True')
# if gHappy("xxgggxyz") != True: print('gHappy("xxgggxyz")  not True')
# if gHappy("xxgggxyg") != False: print('gHappy("xxgggxyg")  not False')
# if gHappy("xxgggxygg") != True: print('gHappy("xxgggxygg")  not True')
# if gHappy("mgm") != False: print('gHappy("mgm")  not False')
# if gHappy("mggm") != True: print('gHappy("mggm")  not True')
# if gHappy("yyygggxyy") != True: print('gHappy("yyygggxyy")  not True')

'''
countTriple
We'll say that a "triple" in a string is a char appearing three times in a row. Return the number of triples 
in the given string. The triples may overlap.
'''
def countTriple(text):
    if len(text) < 3:
        return 0
    counter = 0
    for o in range(len(text) -2):
        if text[o] == text[o+1] == text[o+2]:
            counter += 1
    return counter


# if countTriple("abcXXXabc") != 1: print('countTriple("abcXXXabc")  not 1')
# if countTriple("xxxabyyyycd") != 3: print('countTriple("xxxabyyyycd")  not 3')
# if countTriple("a") != 0: print('countTriple("a")  not 0')
# if countTriple("") != 0: print('countTriple("")  not 0')
# if countTriple("XXXabc") != 1: print('countTriple("XXXabc")  not 1')
# if countTriple("XXXXabc") != 2: print('countTriple("XXXXabc")  not 2')
# if countTriple("XXXXXabc") != 3: print('countTriple("XXXXXabc")  not 3')
# if countTriple("222abyyycdXXX") != 3: print('countTriple("222abyyycdXXX")  not 3')
# if countTriple("abYYYabXXXXXab") != 4: print('countTriple("abYYYabXXXXXab")  not 4')
# if countTriple("abYYXabXXYXXab") != 0: print('countTriple("abYYXabXXYXXab")  not 0')
# if countTriple("abYYXabXXYXXab") != 0: print('countTriple("abYYXabXXYXXab")  not 0')
# if countTriple("122abhhh2") != 1: print('countTriple("122abhhh2")  not 1')

'''
sumDigits
Given a string, return the sum of the digits 0-9 that appear in the string, ignoring all other characters. 
Return 0 if there are no digits in the string. (Note: Character.isDigit(char) tests if a char is one of the chars '0', 
'1', .. '9'. Integer.parseInt(string) converts a string to an int.)
'''
def sumDigits(text):
    digits = [0]
    for o in range(len(text)):
        if text[o].isdigit():
            digits += [int(text[o])]
    return sum(digits)


# if sumDigits("aa1bc2d3") != 6: print('sumDigits("aa1bc2d3")  not 6')
# if sumDigits("aa11b33") != 8: print('sumDigits("aa11b33")  not 8')
# if sumDigits("Chocolate") != 0: print('sumDigits("Chocolate")  not 0')
# if sumDigits("5hoco1a1e") != 7: print('sumDigits("5hoco1a1e")  not 7')
# if sumDigits("123abc123") != 12: print('sumDigits("123abc123")  not 12')
# if sumDigits("") != 0: print('sumDigits("")  not 0')
# if sumDigits("Hello") != 0: print('sumDigits("Hello")  not 0')
# if sumDigits("X1z9b2") != 12: print('sumDigits("X1z9b2")  not 12')
# if sumDigits("5432a") != 14: print('sumDigits("5432a")  not 14')

'''
sameEnds
Given a string, return the longest substring that appears at both the beginning and end of the string 
without overlapping. For example, sameEnds("abXab") is "ab".
'''
# # this will check every possible combination
# def sameEnds(text):
#     def is_A_in_B_twice(a, b):
#         if not a:
#             return False
#         counter = 0
#         i = 0
#         while i < (len(b)):
#             if a == b[i:i + len(a)]:
#                 counter += 1
#                 i += len(a)
#                 continue
#             i += 1
#         if counter < 2:
#             return False
#         return True
#     max_counter = 0
#     max_text = ""
#     for o in range(len(text) + 1):
#         for i in range(len(text) + 1):
#             if is_A_in_B_twice(text[o:i], text) == True:
#                 if max_counter < len(text[o:i]):
#                     max_counter = len(text[o:i])
#                     max_text = text[o:i]
#     return max_text

# This will check if only the beginning is matching to an end
def sameEnds(text):
    def is_A_in_B_twice(a, b):
        if not a:
            return False
        counter = 0
        i = 0
        while i < (len(b)):
            if a == b[i:i + len(a)]:
                counter += 1
                i += len(a)
                continue
            i += 1
        if counter < 2:
            return False
        return True
    max_counter = 0
    max_text = ""
    for o in range(len(text) + 1):
        if is_A_in_B_twice(text[0:o], text) == True:
            if max_counter < len(text[0:o]):
                max_counter = len(text[0:o])
                max_text = text[0:o]
    return max_text


# if sameEnds("abXYab")  != "ab" :print('sameEnds("abXYab")  not "ab"')
# if sameEnds("xx")  != "x" :print('sameEnds("xx")  not "x"')
# if sameEnds("xxx")  != "x" :print('sameEnds("xxx")  not "x"')
# if sameEnds("xxxx")  != "xx" :print('sameEnds("xxxx")  not "xx"')
# if sameEnds("javaXYZjava")  != "java" :print('sameEnds("javaXYZjava")  not "java"')
# if sameEnds("javajava")  != "java" :print('sameEnds("javajava")  not "java"')
# if sameEnds("xavaXYZjava")  != "" :print('sameEnds("xavaXYZjava")  not ""')
# if sameEnds("Hello! and Hello!")  != "Hello!" :print('sameEnds("Hello! and Hello!")  not "Hello!"')
# if sameEnds("x")  != "" :print('sameEnds("x")  not ""')
# if sameEnds("")  != "" :print('sameEnds("")  not ""')
# if sameEnds("abcb")  != "" :print('sameEnds("abcb")  not ""')
# if sameEnds("mymmy")  != "my" :print('sameEnds("mymmy")  not "my"')

'''
mirrorEnds
Given a string, look for a mirror image (backwards) string at both the beginning and end of the 
given string. In other words, zero or more characters at the very begining of the given string, 
and at the very end of the string in reverse order (possibly overlapping). For example, the string 
"abXYZba" has the mirror end "ab".
'''
def mirrorEnds(text):
    def is_A_starting_in_B(a, b):
        for i in range(len(b)):
            if a == b[0:i + len(a)]:
                return True
        return False
    reverse_text = text[::-1]
    max_counter = 0
    max_text = ""
    for o in range(len(text) + 1):
        if is_A_starting_in_B(text[0:o], reverse_text) == True:
            if max_counter < len(text[0:o]):
                max_counter = len(text[0:o])
                max_text = text[0:o]
    return max_text


# if mirrorEnds("abXYZba") != "ab": print('mirrorEnds("abXYZba")  not "ab"')
# if mirrorEnds("abca") != "a": print('mirrorEnds("abca")  not "a"')
# if mirrorEnds("aba") != "aba": print('mirrorEnds("aba")  not "aba"')
# if mirrorEnds("abab") != "": print('mirrorEnds("abab")  not ""')
# if mirrorEnds("xxx") != "xxx": print('mirrorEnds("xxx")  not "xxx"')
# if mirrorEnds("xxYxx") != "xxYxx": print('mirrorEnds("xxYxx")  not "xxYxx"')
# if mirrorEnds("Hi and iH") != "Hi ": print('mirrorEnds("Hi and iH")  not "Hi "')
# if mirrorEnds("x") != "x": print('mirrorEnds("x")  not "x"')
# if mirrorEnds("") != "": print('mirrorEnds("")  not ""')
# if mirrorEnds("123and then 321") != "123": print('mirrorEnds("123and then 321")  not "123"')
# if mirrorEnds("band andab") != "ba": print('mirrorEnds("band andab")  not "ba"')

'''
maxBlock
Given a string, return the length of the largest "block" in the string. A block is a run of adjacent chars 
that are the same.
'''

def maxBlock(text):
    max_counter = 0
    for o in range(len(text)):
        counter = 1
        if counter >= max_counter: # if there is only different characters in the string
            max_counter = counter
        for i in range(o,len(text)-1):
            if text[i] == text[i+1]:
                counter += 1
                if counter >= max_counter:
                    max_counter = counter
            elif text[i] != text[i+1]:
                break
    return max_counter


# if maxBlock("hoopla") != 2: print('maxBlock("hoopla")  not 2')
# if maxBlock("abbCCCddBBBxx") != 3: print('maxBlock("abbCCCddBBBxx")  not 3')
# if maxBlock("") != 0: print('maxBlock("")  not 0')
# if maxBlock("xyz") != 1: print('maxBlock("xyz")  not 1')
# if maxBlock("xxyz") != 2: print('maxBlock("xxyz")  not 2')
# if maxBlock("xyzz") != 2: print('maxBlock("xyzz")  not 2')
# if maxBlock("abbbcbbbxbbbx") != 3: print('maxBlock("abbbcbbbxbbbx")  not 3')
# if maxBlock("XXBBBbbxx") != 3: print('maxBlock("XXBBBbbxx")  not 3')
# if maxBlock("XXBBBBbbxx") != 4: print('maxBlock("XXBBBBbbxx")  not 4')
# if maxBlock("XXBBBbbxxXXXX") != 4: print('maxBlock("XXBBBbbxxXXXX")  not 4')
# if maxBlock("XX2222BBBbbXX2222") != 4: print('maxBlock("XX2222BBBbbXX2222")  not 4')

'''
sumNumbers
Given a string, return the sum of the numbers appearing in the string, ignoring all other characters. 
A number is a series of 1 or more digit chars in a row. (Note: Character.isDigit(char) tests if a char
is one of the chars '0', '1', .. '9'. Integer.parseInt(string) converts a string to an int.)
'''
def sumNumbers(text):
    int_list = []
    string_of_ints = ""
    for o in range(len(text)):
        if text[o].isnumeric() == True:
            string_of_ints += text[o]
            if o == (len(text)-1):
                int_list += [int(string_of_ints)]
        else:
            # only apply to the array if some values have been populated in the string of ints
            if string_of_ints != "": 
                int_list += [int(string_of_ints)]
            string_of_ints = ""
    return sum(int_list)


# if sumNumbers("abc123xyz") != 123: print('sumNumbers("abc123xyz")  not 123')
# if sumNumbers("aa11b33") != 44: print('sumNumbers("aa11b33")  not 44')
# if sumNumbers("7 11") != 18: print('sumNumbers("7 11")  not 18')
# if sumNumbers("Chocolate") != 0: print('sumNumbers("Chocolate")  not 0')
# if sumNumbers("5hoco1a1e") != 7: print('sumNumbers("5hoco1a1e")  not 7')
# if sumNumbers("5$$1;;1!!") != 7: print('sumNumbers("5$$1;;1!!")  not 7')
# if sumNumbers("a1234bb11") != 1245: print('sumNumbers("a1234bb11")  not 1245')
# if sumNumbers("") != 0: print('sumNumbers("")  not 0')
# if sumNumbers("a22bbb3") != 25: print('sumNumbers("a22bbb3")  not 25')

'''
notReplace
Given a string, return a string where every appearance of the lowercase word "is" has been replaced 
with "is not". The word "is" should not be immediately preceeded or followed by a letter -- so for 
example the "is" in "this" does not count. (Note: Character.isLetter(char) tests if a char is a letter.)
'''

def notReplace(text):
    o = 2
    while o <= len(text):
        # print(o)
        if o == 2 and len(text) == 2 and text[0:2] == "is":
            text = text[0:o] + " not" + text[o:]
            o += 4
        elif o == 2 and text[0:2] == "is" and text[o].isalpha() != True:
            text = text[0:o] + " not" + text[o:]
            o += 4
        elif o > 2 and o < len(text) and text[o-3].isalpha() != True and text[o-2:o] == "is" and text[o].isalpha() != True:
            text = text[0:o] + " not" + text[o:]
            o += 4
        elif o == len(text) and text[o-3].isalpha() != True and text[o-2:o] == "is":
            text = text[0:o] + " not" + text[o:]
            o += 4
        o += 1
    return text


# if notReplace("is test") != "is not test": print('notReplace("is test")  not "is not test"')
# if notReplace("is-is") != "is not-is not": print('notReplace("is-is")  not "is not-is not"')
# if notReplace("This is right") != "This is not right": print('notReplace("This is right")  not "This is not right"')
# if notReplace("This is isabell") != "This is not isabell": print('notReplace("This is isabell")  not "This is not isabell"')
# if notReplace("") != "": print('notReplace("")  not ""')
# if notReplace("is") != "is not": print('notReplace("is")  not "is not"')
# if notReplace("isis") != "isis": print('notReplace("isis")  not "isis"')
# if notReplace("Dis is bliss is") != "Dis is not bliss is not": print('notReplace("Dis is bliss is")  not "Dis is not bliss is not"')
# if notReplace("is his") != "is not his": print('notReplace("is his")  not "is not his"')
# if notReplace("xis yis") != "xis yis": print('notReplace("xis yis")  not "xis yis"')
# if notReplace("AAAis is") != "AAAis is not": print('notReplace("AAAis is")  not "AAAis is not"')

