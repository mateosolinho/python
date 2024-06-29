from calcs import calcular_empuje_cohete
from formats import format_empuje

if __name__ == "__main__":
    m_flujo = float(input("Ingrese la tasa de flujo másico del combustible en kg/s: "))
    i_sp = float(input("Ingrese el impulso del motor en segundos: "))
    g0 = 9.81
    
    empuje = calcular_empuje_cohete(m_flujo, i_sp, g0)
    formatted_empuje = format_empuje(empuje)

    print(formatted_empuje)
