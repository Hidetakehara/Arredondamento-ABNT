import math
from decimal import Decimal

def arredondar_ABNT(numero, casas_decimais):
    fator = 10 ** casas_decimais
    numero_ajustado = numero * fator
    inteiro = int(numero_ajustado)
    resto = numero_ajustado - inteiro

    if abs(resto - 0.5) < 1e-12:  # caso especial 0.5
        if inteiro % 2 == 0:
            return inteiro / fator
        else:
            return (inteiro + 1) / fator
    elif resto < 0.5:
        return inteiro / fator
    else:
        return (inteiro + 1) / fator

def casas_para_arredondar(numero, algarismos_significativos):
    if numero == 0:
        return 0
    ordem_magnitude = int(math.floor(math.log10(abs(numero))))
    casas_decimais = algarismos_significativos - 1 - ordem_magnitude
    return max(0, casas_decimais)

def contar_significativos(n):
    s = f"{n:.15g}"
    s = s.strip().replace('.', '')
    s = s.lstrip('0')
    return len(s)

def menor_casas_decimais_var(*numeros):
    casas = []
    for n in numeros:
        s = str(n)
        if "." in s:
            casas.append(len(s.split(".")[1]))
        else:
            casas.append(0)
    return min(casas)

def soma_ABNT_var(*numeros):
    casas_deci = menor_casas_decimais_var(*numeros)
    resultado = sum(numeros)
    return arredondar_ABNT(resultado, casas_deci)

def subtrai_ABNT_var(*numeros):
    casas_deci = menor_casas_decimais_var(*numeros)
    resultado = numeros[0]
    for n in numeros[1:]:
        resultado -= n
    return arredondar_ABNT(resultado, casas_deci)

def multiplica_ABNT_var(*numeros):
    algarismos = min([contar_significativos(n) for n in numeros])
    resultado = 1
    for n in numeros:
        resultado *= n
    casas_deci = casas_para_arredondar(resultado, algarismos)
    return arredondar_ABNT(resultado, casas_deci)

def divide_ABNT_var(*numeros):
    resultado = numeros[0]
    for n in numeros[1:]:
        if n == 0:
            raise ValueError("Divisão por zero não é permitida.")
        resultado /= n
    algarismos = min([contar_significativos(n) for n in numeros])
    casas_deci = casas_para_arredondar(resultado, algarismos)
    return arredondar_ABNT(resultado, casas_deci)


# Testes
print(soma_ABNT_var(4.11, 1, 2.345))       # Esperado: 7.5
print(subtrai_ABNT_var(10.55, 2.3, 1.25))  # Esperado: 7.0
print(multiplica_ABNT_var(4.56, 1.4, 2))   # Esperado: 12.8
print(divide_ABNT_var(786.74, 3.57, 2))    # Esperado: ~110
