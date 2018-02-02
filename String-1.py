def hello_name(name):
    return "Hello {}!".format(name)
# print(hello_name("Toffe"))
#
# def hello_name(name):
#     return "Hello " + name + "!"
# print(hello_name("Toffe"))

def make_abba(a,b):
    return "{}{}{}{}".format(a,b,b,a)
# print(make_abba("Joo","Ei"))
#
def make_abba(a,b):
    return a + b + b + a
# print(make_abba("Joo","Ei"))
#
def make_tags(a,b):
    return "<{}>{}</{}>".format(a,b,a)
# print(make_tags("i","Yay"))

def make_out_word(out,word):
    return (out[:len(out) // 2]) + word + (out[len(out) // 2:])
# print(make_out_word("<<>>","Yay"))

def extra_end(str):
    return str[-2:] * 3
# print(extra_end("lolllolo"))

def first_two(str):
    return str[:2]
# print(first_two("word"))

def first_half(str):
    length = len(str) // 2
    return (str[:length])
# print(first_half("Elisa"))

def without_end(str):
    return str[1:-1]
# print(without_end("Jotain"))

def combo_string(a,b):
    if a == "" :
        return b
    elif b == "":
        return a
    elif len(a) > len(b):
        return b + a + b
    elif len(a) < len(b):
        return a + b + a
# print(combo_string('Hello', 'hi'))
# print(combo_string('hi', 'Hello'))

def non_start(a,b):
    return a[1::] + b[1::]
# print(non_start("Hello","There"))

def left2(str):
    return str[2:] + str[:2]
# print(left2("Hello"))
