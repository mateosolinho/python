def calcular_empuje_cohete(m_flujo, i_sp, g0=9.87):
    e_motor = m_flujo * i_sp * g0

    return e_motor