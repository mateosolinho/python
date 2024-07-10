import random

def game():
    l = input("\nSelect a limit number: ")
    limit = check_number(l)
    random_number = random.randint(1, limit)
    print(f"\n[+] You must find a number between 1 and {limit}")
    print(f"[+] You have 5 chances to choose the right one")
    n = -1
    lives = 5
    while random_number != n:
        number = input("\nInsert your number: ")
        n = check_number(number)
        lives -= 1
        if n is None:
            continue # El "continue" hace que el bucle pase a la siguiente iteración
        if n < random_number:
            print('\nSorry, guess again. Too Low')
            print(f'Remaining Lives: {lives}')
        elif n > random_number:
            print('\nSorry, guess again. Too high')
            print(f'Remaining Lives: {lives}')
        elif n == random_number:
            print('Congratulations!')
        elif lives == 0:
            print('Game Over, no opportunities left')
    return

def check_number(n):
    try:
        return int(n)
    except ValueError:
        print("Formato incorrecto, introduce un número entero")
        return None

if __name__ == "__main__":
    game()