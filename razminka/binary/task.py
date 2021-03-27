def diving(__x, __y):
    return __x % __y == 0


def toBinary(x):
    string = ""
    ends = [1, 0]
    s1 = "1"
    s0 = "0"
    while True:
        if diving(x, 2):
            string = string + s0
        else:
            string = string + s1
        x = x // 2
        if x in ends:
            string = string + str(x)
            break
    return string


def reverseStr(string: str):
    strList = list(string)
    rstring = ""
    strList.reverse()
    for letter in strList:
        rstring = rstring + letter
    return rstring
def abinary(t:str):
    rstring=""
    for letter in list(t):
        rstring=rstring+" "+reverseStr(toBinary(ord(letter)))
    return rstring

x = input("enter number to convert: ")
print(abinary(x))
