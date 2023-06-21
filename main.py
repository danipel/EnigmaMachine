# CÓDIGO ESCRITO POR: DANIEL PELAEZ CHICA
# CODED BY: DANIEL PELAEZ CHICA

from components.reflectors import *
from actions.menu_actions import *


alphabet = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'Á', 'É', 'Í', 'Ó', 'Ú', 'á', 'é', 'í', 'ó',
            'ú', 'Ü', 'ü', '_', '-', '.', ',', ';', ':', ' ', '"', '¿', '?', '¡', '!', '«', '»', '(', ')', '[', ']',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '—', "'", 'ï', 'Ï', 'à', 'ù', '*', '/', "%", '@', '#',
            '$', '&', '\n')
# 108 chars

#  Libro de Don Quijote usando 17 rotores: 6:03 minutos


def main():
    print("BIENVENIDO A LA MÁQUINA ENIGMA ヾ(^▽^*)")
    rotors = define_rotors()
    gray_list = gray_letters(rotors)  # Determina la letra de cada rotor que hace girar al rotor siguiente
    reflector = create_reflector()
    option = str(input("¿Desea ver el reflector y los rotores? s/n")).lower()
    if option == 's':
        show_rotors_and_reflector(rotors, reflector, gray_list)
    conf = initial_conf(rotors)
    option = int(input("Ingrese 1 para encriptar el archivo o 2 para ingresar una frase para encriptar 1/2 "))
    if option == 1:
        encrypt_archive(conf, reflector, gray_list, rotors)
    elif option == 2:
        encrypt_input(conf, reflector, gray_list, rotors)


main()
