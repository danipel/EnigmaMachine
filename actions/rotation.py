alphabet = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'Á', 'É', 'Í', 'Ó', 'Ú', 'á', 'é', 'í', 'ó',
            'ú', 'Ü', 'ü', '_', '-', '.', ',', ';', ':', ' ', '"', '¿', '?', '¡', '!', '«', '»', '(', ')', '[', ']',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '—', "'", 'ï', 'Ï', 'à', 'ù', '*', '/', "%", '@', '#',
            '$', '&', '\n')
# 108 chars


def limit_sum(num):
    if num == len(alphabet):  # len(alphabet):
        num = - len(alphabet)
    else:
        num = 1
    return num


def limit(num):
    if num >= len(alphabet):
        return num - len(alphabet)
    else:
        return num


def rotations(num_conf, gray_list):
    num_conf[0] += limit_sum(num_conf[0])
    for index in range(0, len(num_conf) - 1):
        if num_conf[index] == limit(gray_list[index] + 1):
            num_conf[index + 1] += limit_sum(num_conf[index + 1])
    return num_conf


def initial_conf(rotors):
    conf = []
    print("Por favor, ingrese la configuración inicial de los rotores")
    for index in range(0, len(rotors)):
        print("Rotor ", index + 1, ":")
        conf.append(str(input()))
    return conf


def indexing_conf(conf):
    numeric_conf = []
    for letter in conf:
        numeric_conf.append(alphabet.index(letter))
    return numeric_conf
