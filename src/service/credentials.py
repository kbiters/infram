import json
from math import sqrt

from src.service.constants import Credentials, Map
from src.service.translator import translate

# Variables que nunca deben ser revelados.
VAR_Y = "mimnaugig.iiasa"
EXPONENT_1 = "m"
EXPONENT_2 = "u"


def check_session():
    """
    First we show the information and place, where they can get the credential, then
    to the 2 variables, we put the KEYs that the user entered by keyboard and finally
    we close with an "if" which makes the comparison of the result that gave us the
    function "math_operation()" with the first hash that the user entered, if it matches,
    then it returns "True" and gives access to the user so he can execute the functions
    of the BOT.
    :return:
    """
    try:
        first_hash, second_hash = get_credentials()
        decryp_hash1 = decryptor(first_hash, Map.ENCRYPTOR_MAP)
        decryp_hash2 = decryptor(second_hash, Map.ENCRYPTOR_MAP)
        if decryp_hash1 == math_operation(decryp_hash2):
            print(translate(Credentials.OK))
            return True
        else:
            print(translate(Credentials.INFO))

            first_hash, second_hash = set_user_first_hash(), set_user_second_hash()
            decryp_hash1 = decryptor(list(first_hash.lower()), Map.ENCRYPTOR_MAP)
            decryp_hash2 = decryptor(list(second_hash.lower()), Map.ENCRYPTOR_MAP)

            if decryp_hash1 == math_operation(decryp_hash2):
                save_credentials(first_hash, second_hash)
                print(translate(Credentials.OK))
                return True
            else:
                return False
    except OSError as error:
        print(error)


def decrypt_vars_private():
    """
    Function defined to decrypt the 3 variables that are not given to the user,
    once we have the second variable entered by the user and the 3 private variables
    decrypted, then we proceed to return the numerical values of each decrypted variable.
    :return:
    """
    try:
        VAR_Y_decrypt = decryptor(list(VAR_Y.lower()), Map.ENCRYPTOR_MAP)
        EXPONENT_1_decrypt = decryptor(list(EXPONENT_1.lower()), Map.ENCRYPTOR_MAP)
        EXPONENT_2_decrypt = decryptor(list(EXPONENT_2.lower()), Map.ENCRYPTOR_MAP)

        assert VAR_Y_decrypt and EXPONENT_1_decrypt and EXPONENT_2_decrypt is not None
        return VAR_Y_decrypt, EXPONENT_1_decrypt, EXPONENT_2_decrypt
    except OSError as error:
        print(error)


def math_operation(decrypted_second_hash):
    """
    Function that receives by parameter the segment of numbers that the message returns
    when decrypted and performs the following equation: Square root of "VAR_X(second Hash
    entered by user)" raised to "EXPONENT_1(Private number)" + "VAR_Y(Private number)"
    raised to "EXPONENT_2(Private number)" and the result is returned.
    :param decrypted_second_hash:
    :return:
    """
    try:
        b, c, d = decrypt_vars_private()
        a = float(decrypted_second_hash)
        e = sqrt(a ** int(c) + float(b) ** int(d))
        return str(round(e, ))
    except OSError as error:
        print(error)


def decryptor(x, d):
    """
    Function used to decrypt, the first parameter is the encrypted message and the second
    parameter is the dictionary with which we will decrypt the message, first we go through
    the size of the code and then the size of the dictionary when it is fulfilled that the
    letter of the code is equal to the letter of the dictionary, it is replaced by the
    corresponding number.
    :param x:
    :param d:
    :return:
    """
    try:
        for i in range(len(x)):
            for j in range(10):
                if x[i] == d.get(j):
                    x[i] = str(j)
        return ''.join(x)
    except OSError as error:
        print(error)


def set_user_first_hash():
    """
    The user enters the first encrypted hash.
    :return:
    """
    try:
        return input(translate(Credentials.SET_FIRST))
    except OSError as error:
        print(error)


def set_user_second_hash():
    """
    The user enters the second encrypted hash.
    :return:
    """
    try:
        return input(translate(Credentials.SET_SECOND))
    except OSError as error:
        print(error)


def get_credentials():
    with open('json/credentials.json') as file:
        dat = json.load(file)
        for credentials in dat["credentials"]:
            first_hash = credentials['cred1']
            second_hash = credentials['cred2']
        return list(first_hash.lower()), list(second_hash.lower())


def save_credentials(credential1, credential2):
    data = {'credentials': []}
    data["credentials"].append({
        'cred1': credential1,
        'cred2': credential2,
    })

    with open('json/credentials.json', 'w') as f:
        json.dump(data, f)

# SESSION_KEY_ENCRIPTADA = mseassunioeasomi
# SESSION_KEY = 4819883657198745 <--- la funcion math_operation() devuelve exactamente ese numero

# VAX_X_ENCRIPTADA = namgiuee.olmo
# VAR_X = 69425311.7047

# VAX_Y_ENCRIPTADA = mimnaugig.iiasa
# VAR_Y = 454693252.55989

# EXPONENT_1 = m
# EXPONENT_1 = 4

# EXPONENT_2 = u
# EXPONENT_2 = 3
