from calcs import calcular_empuje_cohete
from formats import format_empuje

def menu_principal():
    print("\n--- Rocket Calculator ---")
    print("1. Motores")
    print("2. Salir")

def menu_motores():
     print("\n--- Calculos Motores ----")
     print("1. Calcular Empuje")
     print("2. Calcular Impulso Específico")
     print("3. Calcular Tasa de Flujo Másico")
     print("4. Salir")

def ejecutar_motores():
    menu_motores()
    opcion = int(input("Introduce la opcion que quieras "))
    match opcion:
        case 1:
            m_flujo = float(input("Ingrese la tasa de flujo másico del combustible en kg/s: "))
            i_sp = float(input("Ingrese el impulso del motor en segundos: "))
            formatted_empuje = format_empuje(calcular_empuje_cohete(m_flujo, i_sp))
            print(f"\n{formatted_empuje}")
        case 2:
            print()
        case 3:
            print()
        case 4:
            print("Saliendo")

def ejecutar_menu():
    menu_principal()
    opcion = int(input("Introduce la opcion que quieras "))
    while True:
        match opcion:
            case 1:
                ejecutar_motores()
            case 2:
                print()
            case 3:
                print()
            case 4:
                print("Saliendo")
                break