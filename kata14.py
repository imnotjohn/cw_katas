# coding=UTF-8
def dative(word):
    front = ["e", "é", "i", "í", "ö", "ő", "ü", "ű"]
    back = ["a", "á", "o", "ó", "u", "ú"]
    return (word + "nek") if any(str(vowel).decode('latin1') == str((word[-2])).decode('latin1') for vowel in front) else (word + "nak")
    # list = ["a", "e", "i", "o", "u"]
    # return True if any(vowel == word[-1] for vowel in list) else False
