import string

def removepunc(strr):
    strr = strr
    p = string.punctuation
    text = ""
    for char in strr:
        if char not in p:
            text = text+char
    
    return text

