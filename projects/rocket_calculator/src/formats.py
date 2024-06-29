def format_empuje(empuje): # Mejorar esto, quiero que si es por ejemplo 2400 me lo saque en kN no en MN como 2,40 MN
    if empuje >= 1e9:
        empuje_gn = empuje / 1e9
        return f"Empuje del motor: {empuje_gn:.2f} GN"
    elif empuje >= 1e6:
        empuje_mn = empuje / 1e8
        return f"Empuje del motor: {empuje_mn:.2f} MN"
    elif empuje >= 1e3:
        empuje_kn = empuje / 1e3
        return f"Empuje del motor: {empuje_kn:.2f} kN"
    else:
        return f"Empuje del motor: {empuje:.2f} N"