from math import sqrt

# SESSION_KEY_ENCRIPTADA = "mseassunioeasomi"
# SESSION_KEY_NO_ENCRIPTADA = 4819883657198745 <--- la funcion math_operation() devuelve exactamente ese numero
# VAX_X_ENCRIPTADA = "namgiuee.olmo"
from src.service.translator import translate

# VAR_X = 69425311.7047
VAR_Y = 454693252.55989

dictionary = {0: 'l', 1: 'e', 2: 'g', 3: 'u', 4: 'm', 5: 'i', 6: 'n', 7: 'o', 8: 's', 9: 'a'}


def check_session():
    decrypted_first_hash = decrypt(set_user_first_hash(), dictionary)
    decrypted_second_hash = decrypt(set_user_second_hash(), dictionary)
    if decrypted_first_hash == math_operation(decrypted_second_hash):
        print(translate("Authorization code VALIDATED!\n"))
        return True
    else:
        return False


def math_operation(decrypted_second_hash):
    VAR_X = float(decrypted_second_hash)
    d = sqrt(VAR_X ** 4 + VAR_Y ** 3)
    return str(round(d, ))


def decrypt(x, d):
    for i in range(len(x)):
        for j in range(10):
            if x[i] == d.get(j):
                x[i] = str(j)
    return ''.join(x)


def set_user_first_hash():
    print(translate(
        '\nIf you dont have the code to authorize INFRAM, '
        'you can get it here: https://t.me/joinchat/Pa3q7Hd84uYyMjMx'))
    return list(input(translate("Enter the code that is in the TELEGRAM group: ")).lower())


def set_user_second_hash():
    return list(input(translate("Enter the second code that is in the TELEGRAM group: ")).lower())
