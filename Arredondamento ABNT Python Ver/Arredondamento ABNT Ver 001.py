import math
from decimal import Decimal

def arredondar_ABNT(numero, casas_decimais):
    fator = 10 ** casas_decimais
    numero_ajustado = numero * fator
    inteiro = int(numero_ajustado)
    resto = numero_ajustado - inteiro

    if abs(resto - 0.5) < 1e-12:  # caso especial 0.5
        if inteiro % 2 == 0:
            resultado = inteiro / fator
        else:
            resultado = (inteiro + 1) / fator
    elif resto < 0.5:
        resultado = inteiro / fator
    else:
        resultado = (inteiro + 1) / fator

    # 🔑 Ajuste final: se não há casas decimais, retorna int
    if casas_decimais == 0:
        return int(resultado)
    return resultado

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


import unittest

class TestABNT(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(soma_ABNT_var(4.11, 1, 2.345), 7)
    def test_subtracao(self):
        self.assertEqual(subtrai_ABNT_var(10.55, 2.3, 1.25), 7.0)
    def test_multiplicacao(self):
        self.assertEqual(multiplica_ABNT_var(4.56, 1.4, 2), 10)
    def test_divisao(self):
        self.assertEqual(divide_ABNT_var(786.74, 3.57, 2), 100)
    def test_arredondamento_par(self):
        self.assertEqual(arredondar_ABNT(2.5, 0), 2)
    def test_arredondamento_impar(self):
        self.assertEqual(arredondar_ABNT(3.5, 0), 4)

if __name__ == "__main__":
    unittest.main()
