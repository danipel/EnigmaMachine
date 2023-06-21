alphabet = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'Á', 'É', 'Í', 'Ó', 'Ú', 'á', 'é', 'í', 'ó',
            'ú', 'Ü', 'ü', '_', '-', '.', ',', ';', ':', ' ', '"', '¿', '?', '¡', '!', '«', '»', '(', ')', '[', ']',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '—', "'", 'ï', 'Ï', 'à', 'ù', '*', '/', "%", '@', '#',
            '$', '&', '\n')
# 108 chars


def create_file(nombre_archivo, mensaje):
    f = open(nombre_archivo + ".txt", "w")
    frase = mensaje
    f.write(frase)
    f.close()


def read_file():
    f = open("DonPiojote.txt", "r", encoding="utf-8")
    texto = f.read()
    f.close()
    return texto


def list_to_string(encrypted_text):
    info_to_encrypt = ""
    for letter in encrypted_text:
        info_to_encrypt = info_to_encrypt + letter
    return info_to_encrypt


def list_nums_to_string_letters(decrypted_text):
    final_message = ""
    for letter in decrypted_text:
        final_message = final_message + alphabet[alphabet.index(letter)]
    return final_message
