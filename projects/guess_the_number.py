import random

def game():
    random_number = random.randint(1, 10)
    n = -1
    while random_number != n:
        n = int(input("Insert your number: "))
        # n = check_number(number)
        if n < random_number:
            print('Sorry, guess again. Too Low')
        elif n > random_number:
            print('Sorry, guess again. Too high')
        elif n == random_number:
            print('Congratulations!')
    
    return

def check_number():
    error = True
    while error:
        try:
            error = False
        except(ValueError):
            print("Formato incorrecto, introduce un número entero")
    
    return

if __name__ == "__main__":
    game()