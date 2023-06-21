from actions.rotation import rotations

alphabet = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'Á', 'É', 'Í', 'Ó', 'Ú', 'á', 'é', 'í', 'ó',
            'ú', 'Ü', 'ü', '_', '-', '.', ',', ';', ':', ' ', '"', '¿', '?', '¡', '!', '«', '»', '(', ')', '[', ']',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '—', "'", 'ï', 'Ï', 'à', 'ù', '*', '/', "%", '@', '#',
            '$', '&', '\n')
# 108 chars


def check_result(num):
    if num < 0:
        num = num + len(alphabet)
    return num


def run_rotors(num, num_config, rotors):
    for rotor in rotors:
        rotation = num + num_config[rotors.index(rotor)]
        if rotation >= len(alphabet):
            rotation = rotation - len(alphabet)
        #  print("Número ", num, "rotado a", rotation, " después del rotor ", rotors.index(rotor) + 1, ":",
        #  rotor[rotation])
        num = check_result(rotor[rotation] - num_config[rotors.index(rotor)])
    return num


def search_with_value(value, rotor):
    keys = rotor.keys()
    for key in keys:
        if rotor[key] == value:
            return int(key)


def back_run_rotors(num, num_config, rotors):
    for rotor in rotors:
        rotation = num + num_config[rotors.index(rotor)]
        if rotation >= len(alphabet):
            rotation = rotation - len(alphabet)
        #  print("Número ", num, "rotado a", rotation, " después del rotor ", rotors.index(rotor) + 1, ":",
        #      search_with_value(rotation, rotor))
        num = check_result(search_with_value(rotation, rotor) - num_config[rotors.index(rotor)])
    return num


def run_reflector(num, reflector):
    # temp = num
    num = check_result(reflector[num])
    #  print("Número ", temp, " después del reflector :", num)
    return num


#           lista_num    str             dicc       num_list      tuple of diccs
def encrypt(num_config, text_to_encrypt, reflector, gray_letters, rotors):
    encrypted_text = []
    for letter in text_to_encrypt:
        number = alphabet.index(letter)
        num_config = rotations(num_config, gray_letters)
        number = run_rotors(number, num_config, rotors)
        number = run_reflector(number, reflector)
        rotors_list = list(rotors)
        rotors_list.reverse()
        num_config.reverse()
        number = back_run_rotors(number, num_config, rotors_list)
        num_config.reverse()
        encrypted_text.append(alphabet[number])
        #  print(encrypted_text)
    #  print(encrypted_text)
    return encrypted_text
