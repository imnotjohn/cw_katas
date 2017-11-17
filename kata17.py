# You need to write regex that will validate a password to make sure it meets the following criteria:
#
# At least six characters long
# contains a lowercase letter
# contains an uppercase letter
# contains a number
# Valid passwords will only be alphanumeric characters.
#
#
import re

regex=[r"[A-Z]", r"[a-z]", r"[0-9]"]

def checkPassword(p):
    if (type(p) is str and len(p)>5 and re.search(str(regex[0]), p, 1) and re.search(str(regex[1]), p, 1) and re.search(str(regex[2]), p, 1)):
        return True
    else:
        return False
