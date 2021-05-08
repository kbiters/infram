from math import sqrt

from src.json.credentials import save_credentials, get_credentials
from src.service.constants import Credentials, Map
from src.service.translator import translate

# Variables que nunca deben ser revelados.
VAR_Y = "mimnaugig.iiasa"
EXPONENT_1 = "m"
EXPONENT_2 = "u"


def check_session():
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
        print(translate(error))


def decrypt_vars_private():
    try:
        VAR_Y_decrypt = decryptor(list(VAR_Y.lower()), Map.ENCRYPTOR_MAP)
        EXPONENT_1_decrypt = decryptor(list(EXPONENT_1.lower()), Map.ENCRYPTOR_MAP)
        EXPONENT_2_decrypt = decryptor(list(EXPONENT_2.lower()), Map.ENCRYPTOR_MAP)

        assert VAR_Y_decrypt and EXPONENT_1_decrypt and EXPONENT_2_decrypt is not None
        return VAR_Y_decrypt, EXPONENT_1_decrypt, EXPONENT_2_decrypt
    except OSError as error:
        print(translate(error))


def math_operation(decrypted_second_hash):
    try:
        b, c, d = decrypt_vars_private()
        a = float(decrypted_second_hash)
        e = sqrt(a ** int(c) + float(b) ** int(d))
        return str(round(e, ))
    except OSError as error:
        print(translate(error))


def decryptor(x, d):
    try:
        for i in range(len(x)):
            for j in range(10):
                if x[i] == d.get(j):
                    x[i] = str(j)
        return ''.join(x)
    except OSError as error:
        print(translate(error))


def set_user_first_hash():
    try:
        return input(translate(Credentials.SET_FIRST))
    except OSError as error:
        print(translate(error))


def set_user_second_hash():
    try:
        return input(translate(Credentials.SET_SECOND))
    except OSError as error:
        print(translate(error))

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
