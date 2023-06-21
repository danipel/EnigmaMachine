import random

alphabet = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'Á', 'É', 'Í', 'Ó', 'Ú', 'á', 'é', 'í', 'ó',
            'ú', 'Ü', 'ü', '_', '-', '.', ',', ';', ':', ' ', '"', '¿', '?', '¡', '!', '«', '»', '(', ')', '[', ']',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '—', "'", 'ï', 'Ï', 'à', 'ù', '*', '/', "%", '@', '#',
            '$', '&', '\n')
# 108 chars


def domain_reflectors(number_1, number_2, number_list):
    if number_1 != number_2 and not (number_1 in number_list):
        return True
    else:
        return False


def create_reflector():
    taken_seats = []
    unions = {}
    confirm = True
    for seat in range(0, len(alphabet)):
        if seat != len(alphabet):
            confirm = True
        if seat in taken_seats:
            confirm = False
        while confirm:
            connect = random.randrange(0, len(alphabet))
            if domain_reflectors(connect, seat, taken_seats) is True:
                unions[seat] = connect
                unions[connect] = seat
                taken_seats.append(connect)
                taken_seats.append(seat)
                confirm = False
    return unions
