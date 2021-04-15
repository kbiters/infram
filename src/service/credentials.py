from math import sqrt

from src.service.constants import Credentials, Map
from src.service.translator import translate

# Variables que nunca deben ser revelados.
VAR_Y = 454693252.55989
EXPONENT_1 = 4
EXPONENT_2 = 3


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
    print(translate(Credentials.INFO))
    decrypted_first_hash = decrypt(set_user_first_hash(), Map.ENCRYPTOR_MAP)
    decrypted_second_hash = decrypt(set_user_second_hash(), Map.ENCRYPTOR_MAP)
    if decrypted_first_hash == math_operation(decrypted_second_hash):
        print(translate(Credentials.OK))
        return True
    else:
        return False


def math_operation(decrypted_second_hash):
    """
    Function that receives by parameter the segment of numbers that the message returns
    when decrypted and performs the following equation: Square root of "VAR_X(second Hash
    entered by user)" raised to "EXPONENT_1(Private number)" + "VAR_Y(Private number)"
    raised to "EXPONENT_2(Private number)" and the result is returned.
    :param decrypted_second_hash:
    :return:
    """
    VAR_X = float(decrypted_second_hash)
    d = sqrt(VAR_X ** EXPONENT_1 + VAR_Y ** EXPONENT_2)
    return str(round(d, ))


def decrypt(x, d):
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
    for i in range(len(x)):
        for j in range(10):
            if x[i] == d.get(j):
                x[i] = str(j)
    return ''.join(x)


def set_user_first_hash():
    """
    The user enters the first encrypted hash.
    :return:
    """
    return list(input(translate(Credentials.SET_FIRST)).lower())


def set_user_second_hash():
    """
    The user enters the second encrypted hash.
    :return:
    """
    return list(input(translate(Credentials.SET_SECOND)).lower())


# SESSION_KEY_ENCRIPTADA = mseassunioeasomi
# SESSION_KEY_NO_ENCRIPTADA = 4819883657198745 <--- la funcion math_operation() devuelve exactamente ese numero
# VAX_X_ENCRIPTADA = namgiuee.olmo
# VAR_X = 69425311.7047
