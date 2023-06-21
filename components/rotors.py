import random
alphabet = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'Á', 'É', 'Í', 'Ó', 'Ú', 'á', 'é', 'í', 'ó',
            'ú', 'Ü', 'ü', '_', '-', '.', ',', ';', ':', ' ', '"', '¿', '?', '¡', '!', '«', '»', '(', ')', '[', ']',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '—', "'", 'ï', 'Ï', 'à', 'ù', '*', '/', "%", '@', '#',
            '$', '&', '\n')
# 108 chars


def gray_letters(rotors):
    gray_list = []
    num_rotors = len(rotors)
    while num_rotors != 0:
        gray_list.append(random.randrange(0, len(alphabet)))
        num_rotors -= 1
    return gray_list


def domain_rotors(number, number_list):
    if not (number in number_list):
        return True
    else:
        return False


def create_rotor():
    taken_seats = []
    unions = {}
    confirm = True
    for seat in range(0, len(alphabet)):  #80
        if seat != len(alphabet):  #80
            confirm = True
        while confirm:
            connect = random.randrange(0, len(alphabet))  #80
            if domain_rotors(connect, taken_seats) is True:
                unions[seat] = connect
                taken_seats.append(connect)
                confirm = False
    return unions
