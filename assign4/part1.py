import re
def is_alpha(str0):
    li = re.split(r"[a-zA-Z]+",str0)
    if li == ['','']:
        return True
    else:
        return False

def is_alnum(str0):
    li = re.split(r"[a-zA-Z0-9]+", str0)
    if li == ['', '']:
        return True
    else:
        return False
def startswith(str0, prefix):
    li = re.split(prefix,str0)
    if li[0] == '':
        return True
    else:
        return False
def is_in(str0, str1):
    li = re.split(str1, str0)
    if li[0] == str0:
        return False
    else:
        return True
print(is_alpha("faweda"))
print(is_alnum("2341"))
print(startswith("fwaa","fw"))
print(is_in("fwaa","fwaa"))
