import re

def senha_forte(s):
    numeros = len(re.findall(r'\d', s))
    especiais = len(re.findall(r'[!@#$%^&*()_+\-=\[\]{};\'":\\|,.<>/?]', s))

    if len(s) < 12:
        return False
    if numeros < 3:
        return False
    if especiais < 1:
        return False

    return True