from components.rotors import *
from actions.rotation import *
from actions.encryptation import *
from data.text import *


def encrypt_input(config, reflector, gray_list, rotors):
    encrypted_text = encrypt(indexing_conf(config), str(input("Ingrese el texto a encriptar: ")), reflector, gray_list, rotors)
    decrypt = list_to_string(encrypted_text)
    decrypted_text = encrypt(indexing_conf(config), decrypt, reflector, gray_list, rotors)
    print("Configuración usada: ", config)
    show_in_terminal(encrypted_text, decrypted_text)


def encrypt_archive(config, reflector, gray_list, rotors):
    encrypted_text = encrypt(indexing_conf(config), read_file(), reflector, gray_list, rotors)
    decrypt = list_to_string(encrypted_text)
    decrypted_text = encrypt(indexing_conf(config), decrypt, reflector, gray_list, rotors)
    print("Configuración usada: ", config)
    show_in_archives(encrypted_text, decrypted_text)


def show_in_archives(encrypted, decrypted):
    print("Texto encriptado llevado al archivo")
    encrypted_text = list_nums_to_string_letters(encrypted)
    create_file("encrypted", encrypted_text)
    print("Texto desencriptado llevado al archivo")
    decrypted_text = list_nums_to_string_letters(decrypted)
    create_file("decrypted", decrypted_text)


def show_in_terminal(encrypted, decrypted):
    print("Texto encriptado: ", list_nums_to_string_letters(encrypted))
    print("Texto desencriptado: ", list_nums_to_string_letters(decrypted))


def define_rotors():
    rotors = []
    num_rotors = int(input("¿Cuántos rotores desea emplear? "))
    while num_rotors != 0:
        rotors.append(create_rotor())
        num_rotors -= 1
    return tuple(rotors)


def show_rotors_and_reflector(rotors, reflector, gray_list):
    for rotor in rotors:
        print("Rotor ", rotors.index(rotor) + 1, ": ", rotor)
        print("Letra gris: ", alphabet[gray_list[rotors.index(rotor)]])
    print("Reflector: ", reflector)
