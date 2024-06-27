import string
import random

def password_structure():
    print("\n[#] Select password complexity")
    print("[1] Only letters")
    # 65 - 122
    print("[2] Letters & numbers")
    # 65 - 122
    # 48 - 57
    print("[3] Letters & numbers & simbols")
    # 33 - 126
    try:
        complexity = int(input("[?] Enter the complexity you want (1, 2 or 3): "))
    except(ValueError):
        print("\n[!] Wrong complexity format")
        print("[!] Using default complexity -> Letters & numbers & simbols ")
        complexity = 3

    if complexity not in [1,2,3]:
        print("\n[!] Error, invalid complexity")
        return ""
    else:
        return complexity

def random_generator(length, complexity):
    password = ""

    # Inicialmente caracteres con todas las letras mayus y minus
    caracteres = string.ascii_letters

    # Dependiendo de xomplexity se añaden los caracteres
    if complexity >= 2:
        caracteres += string.digits
    if complexity == 3:
        caracteres += string.punctuation

    # Coge valores random de la lista de caracteres con longitud length
    password = [random.choice(caracteres) for _ in range(length - 1)]

    # Genera un caracter ascii aleatorio
    ascii_char = chr(random.randint(65,122))

    # Posicion del caracter
    rand_pos = random.randint(0, length - 1)

    # Inserta el caracter en la posicion random
    password.insert(rand_pos, ascii_char)

    # Convierte la lista a una cadena
    password = ''.join(password)

    return password

def length_check():
    # print(sys.maxsize)
    pass_length = 16

    try:
        pass_length = int(input("\n[#] Insert your password length: "))
    except(ValueError):
        print("\n[!] Wrong length format")
        print("[!] Using default length -> 16")
    return pass_length

def main():
    length = length_check()
    complexity = password_structure()

    final_pass = random_generator(length, complexity)

    print(f"\n[+] Your password = {final_pass}\n")

if __name__ == "__main__":
    main()